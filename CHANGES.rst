Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

3.0.0a1 (2025-11-19)
--------------------

Breaking changes:


- Replace ``pkg_resources`` namespace with PEP 420 native namespace.
  Support only Plone 6.2 and Python 3.10+. (#3928)


2.0.2 (2025-09-10)
------------------

Internal:


- Update configuration files.
  [plone devs] (6e36bcc4)
- Move distribution to src layout [gforcada] (#4217)


2.0.1 (2024-01-19)
------------------

Internal:


- Update configuration files.
  [plone devs] (237ff4c8)


2.0.0 (2023-04-15)
------------------

Breaking changes:


- Drop python 2 support.
  [gforcada] (#1)


1.1.6 (2023-04-15)
------------------

Internal:


- Update configuration files.
  [plone devs] (5623f8b3)


1.1.5 (2020-04-20)
------------------

Bug fixes:


- Minor packaging updates. (#1)


1.1.4 (2020-03-21)
------------------

Bug fixes:


- Minor packaging updates. [various] (#1)


1.1.3 (2018-11-21)
------------------

Bug fixes:


- Cleanup project level files (setup.py, .travis-ci.yml...) [maurits]
  [gforcada] (#2524)
- Initialized towncrier. [gforcada] (#2548)


1.1.3 (unreleased)
------------------


1.1.2 (2018-11-21)
------------------

Bug fixes:

- Update code to follow Plone styleguide.
  [gforcada]

1.1 (2016-11-01)
----------------

New features:

- Add compatibility with Python 3. [datakurre]


1.0.1 (2016-08-11)
------------------

Fixes:

- Use zope.interface decorator.
  [gforcada]


1.0 (2011-04-30)
----------------

- Use doctest from the stdlib instead of from zope.testing
  [davisagli]


1.0a1 (2009-04-17)
------------------

- Initial release.
