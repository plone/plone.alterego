from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='plone.alterego',
      version=version,
      description="Low level support for dynamic modules",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone schema interface',
      author='Laurence Rowe',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://code.google.com/p/dexterity',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
