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
                raise e
            
            obj = factory(name, self)
            if obj is None:
                raise e
            
            __dict__ = module.__getattribute__(self, '__dict__')
            __dict__[name] = obj
            return obj
            
def create(parent_module, name):
    full_name = '%s.%s' % (parent_module.__name__, name)
    dynamic = DynamicModule(full_name)
    sys.modules[full_name] = dynamic
    setattr(parent_module, name, dynamic)
    return dynamic
    
__all__ = ('create',)