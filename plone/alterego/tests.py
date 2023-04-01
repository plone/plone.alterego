import doctest
import unittest
import zope.component.testing


def test_suite():
    return unittest.TestSuite(
        (
            doctest.DocFileSuite(
                "alterego.txt",
                tearDown=zope.component.testing.tearDown,
            ),
        )
    )
