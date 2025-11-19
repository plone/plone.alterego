from pathlib import Path
from setuptools import setup


version = "3.0.0a1"

long_description = (
    f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}"
)

setup(
    name="plone.alterego",
    version=version,
    description="Low level support for dynamic modules",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Plone schema interface",
    author="Laurence Rowe",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/plone.alterego",
    license="LGPL",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "zope.component",
        "zope.interface",
    ],
    extras_require={"test": []},
    entry_points="""
    # -*- Entry points: -*-
    """,
)
