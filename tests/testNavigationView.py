#
# Test methods used to make ...
#

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Testing import ZopeTestCase
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase import dummy
PloneTestCase.setupPloneSite()

from Products.CMFPlone.utils import _createObjectByType

class TestNavigationView(PloneTestCase.PloneTestCase):
    """Tests the ... """
    pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestNavigationView))
    return suite

if __name__ == '__main__':
    framework()