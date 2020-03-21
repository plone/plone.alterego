# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = '1.1.4'

setup(
    name='plone.alterego',
    version=version,
    description='Low level support for dynamic modules',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGES.rst').read()),
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Framework :: Plone :: 5.2',
        'Framework :: Plone :: Core',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='Plone schema interface',
    author='Laurence Rowe',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone.alterego',
    license='LGPL',
    packages=find_packages(),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.interface',
    ],
    extras_require={
        'test': []
    },
    entry_points="""
    # -*- Entry points: -*-
    """,
)
