# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from nativeberries.content.testing import NATIVEBERRIES_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that nativeberries.content is properly installed."""

    layer = NATIVEBERRIES_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if nativeberries.content is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('nativeberries.content'))

    def test_uninstall(self):
        """Test if nativeberries.content is cleanly uninstalled."""
        self.installer.uninstallProducts(['nativeberries.content'])
        self.assertFalse(self.installer.isProductInstalled('nativeberries.content'))

    def test_browserlayer(self):
        """Test that INativeberriesContentLayer is registered."""
        from nativeberries.content.interfaces import INativeberriesContentLayer
        from plone.browserlayer import utils
        self.assertIn(INativeberriesContentLayer, utils.registered_layers())
