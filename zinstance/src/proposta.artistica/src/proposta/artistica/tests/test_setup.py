# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from proposta.artistica.testing import PROPOSTA_ARTISTICA_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that proposta.artistica is properly installed."""

    layer = PROPOSTA_ARTISTICA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if proposta.artistica is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'proposta.artistica'))

    def test_browserlayer(self):
        """Test that IPropostaArtisticaLayer is registered."""
        from proposta.artistica.interfaces import (
            IPropostaArtisticaLayer)
        from plone.browserlayer import utils
        self.assertIn(IPropostaArtisticaLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PROPOSTA_ARTISTICA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['proposta.artistica'])

    def test_product_uninstalled(self):
        """Test if proposta.artistica is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'proposta.artistica'))

    def test_browserlayer_removed(self):
        """Test that IPropostaArtisticaLayer is removed."""
        from proposta.artistica.interfaces import IPropostaArtisticaLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPropostaArtisticaLayer, utils.registered_layers())
