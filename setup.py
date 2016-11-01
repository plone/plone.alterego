from setuptools import setup, find_packages

version = '1.1'

setup(
    name='plone.alterego',
    version=version,
    description="Low level support for dynamic modules",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    # Get more strings from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Plone schema interface',
    author='Laurence Rowe',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/plone.alterego',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup']),
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
