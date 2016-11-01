# -*- coding: utf-8 -*-
import doctest
import sys
import unittest
import zope.component.testing


SKIP_PYTHON_2 = doctest.register_optionflag('SKIP_PYTHON_2')
SKIP_PYTHON_3 = doctest.register_optionflag('SKIP_PYTHON_3')


class PolyglotOutputChecker(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        if optionflags & SKIP_PYTHON_3 and sys.version_info >= (3,):
            return True
        elif optionflags & SKIP_PYTHON_2:
            return True

        return doctest.OutputChecker.check_output(
            self, want, got, optionflags)


def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            'alterego.txt',
            tearDown=zope.component.testing.tearDown,
            checker=PolyglotOutputChecker(),
        ),
    ))
