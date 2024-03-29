==============
plone.alterego
==============

Now you see it, it now you don't!

This package defines a dynamic module type that lets you create objects in the
dynamic module on demand.

Usage
-----

To use this package, you should:

- Identify an appropriate parent module where the dynamic module will live.

- Ensure that plone.alterego.dynamic.create() is called with this module and a dynamic module name. 
  Typically, you'd do this in the parent module itself, so that the dynamic module is instantiated as soon as the parent module is imported.

- Register a named utility providing IDynamicObjectFactory. 
  The name should be the same as the full dotted path to the dynamic module. 
  This utility will be responsible for creating the objects that inhabit the dynamicmodule.

Example
-------

For a more fully-featured example, see the alterego.txt doctest.

Let's say we have a generic content class that should get a unique interface
for each instance.

.. code-block:: python

    >>> from zope import interface
    >>> class IContent(interface.Interface):
    ...     pass
    >>> class Content(object):
    ...     interface.implements(IContent)

    >>> c1 = Content()

To create the unique interface, we will use a dynamic module. There is a
helper method to make this easier. It takes a parent module and a name as
arguments:

.. code-block:: python

    >>> from plone.alterego.dynamic import create
    >>> dynamic = create('plone.alterego.tests.dynamic')

We can now import this module:

.. code-block:: python

    >>> from plone.alterego.tests import dynamic

To make objects on demand, we'll need to register a utility that can act
as a factory.

.. code-block:: python

    >>> from plone.alterego.interfaces import IDynamicObjectFactory
    >>> from zope.interface.interface import InterfaceClass
    >>> class InterfaceOnDemand(object):
    ...     interface.implements(IDynamicObjectFactory)
    ...
    ...     def __call__(self, name, module):
    ...         schema = InterfaceClass(name, (interface.Interface,), __module__=module.__name__)
    ...         setattr(module, name, schema)
    ...         return schema

This utility should have a name that corresponds to the full,
dotted name to the dynamic module. This way, we can have different factories
for different dynamic modules. We'd register this in ZCML like so:

.. code-block:: XML

    <utility
        name="plone.alterego.tests.dynamic"
        provides="plone.alterego.interfaces.IDynamicObjectFactory"
        factory=".factory.InterfaceOnDemand"
        />

From this point forward, when we access an attribute of the dynamic module,
the factory will be used:

.. code-block:: python

    >>> dynamic.IOne
    <InterfaceClass plone.alterego.tests.dynamic.IOne>

Note that so long as the setattr() call above is executed, the factory is
called only once. That is, you'll always get the same object each time you
access a given attribute of the dynamic module.

