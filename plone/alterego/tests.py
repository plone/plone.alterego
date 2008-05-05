import unittest

import zope.testing.doctest
import zope.component.testing
import zope.app.testing.placelesssetup

import plone.alterego

def test_suite():
    return unittest.TestSuite((
        
        zope.testing.doctest.DocFileSuite('alterego.txt',
                     # setUp=setUp,
                     tearDown=zope.component.testing.tearDown),
        

        # zope.testing.doctest.DocTestSuite(plone.alterego,
        #             # setUp=setUp,
        #             tearDown=zope.app.testing.placelesssetup.tearDown),
                     
        ))