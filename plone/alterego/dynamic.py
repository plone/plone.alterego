import sys
from new import module

from zope.interface import implements
from zope.component import queryUtility

from plone.alterego.interfaces import IDynamicModule
from plone.alterego.interfaces import IDynamicObjectFactory

class DynamicModule(module):
    """A module that can create objects on the fly.
    """
    
    implements(IDynamicModule)

    def __getattribute__(self, name):
        try:
            return module.__getattribute__(self, name)
        except AttributeError, e:
            
            __name__ = module.__getattribute__(self, '__name__')
            factory = queryUtility(IDynamicObjectFactory, name=__name__)
            if factory is None:
                raise AttributeError("Cannot find dynamic object factory for module %s" % __name__)
            
            obj = factory(name, self)
            if obj is None:
                raise e
            
            __dict__ = module.__getattribute__(self, '__dict__')
            __dict__[name] = obj
            return obj
            
def create(dotted_name):
    dynamic = DynamicModule(dotted_name)
    sys.modules[dotted_name] = dynamic
    return dynamic
    
__all__ = ('create',)