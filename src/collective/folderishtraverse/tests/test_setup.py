# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.folderishtraverse.testing import COLLECTIVE_FOLDERISHTRAVERSE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.folderishtraverse is properly installed."""

    layer = COLLECTIVE_FOLDERISHTRAVERSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.folderishtraverse is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.folderishtraverse'))

    def test_browserlayer(self):
        """Test that ICollectiveFolderishtraverseLayer is registered."""
        from collective.folderishtraverse.interfaces import (
            ICollectiveFolderishtraverseLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveFolderishtraverseLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FOLDERISHTRAVERSE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.folderishtraverse'])

    def test_product_uninstalled(self):
        """Test if collective.folderishtraverse is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.folderishtraverse'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveFolderishtraverseLayer is removed."""
        from collective.folderishtraverse.interfaces import ICollectiveFolderishtraverseLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveFolderishtraverseLayer, utils.registered_layers())
