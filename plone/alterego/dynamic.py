# -*- coding: utf-8 -*-
from plone.alterego.interfaces import IDynamicModule
from plone.alterego.interfaces import IDynamicObjectFactory
from types import ModuleType
from zope.component import queryUtility
from zope.interface import implementer

import sys


@implementer(IDynamicModule)
class DynamicModule(ModuleType):
    """A module that can create objects on the fly.
    """

    def __getattr__(self, name):

        if name == '__path__':
            raise AttributeError('Dynamic modules do not have __path__')

        factory = queryUtility(IDynamicObjectFactory, name=self.__name__)
        if factory is None:
            raise AttributeError(
                'Cannot find dynamic object factory for module {0}'.format(
                    self.__name__,
                )
            )

        obj = factory(name, self)
        if obj is None:
            raise AttributeError(
                'Dynamic module factory did not want to create '
                '{0} in {1}'.format(name, self.__name__)
            )

        return obj


def create(dotted_name):
    dynamic = DynamicModule(dotted_name)
    sys.modules[dotted_name] = dynamic
    return dynamic


__all__ = ('create',)
