# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from proposta.artistica.testing import PROPOSTA_ARTISTICA_INTEGRATION_TESTING  # noqa
from proposta.artistica.interfaces import IPropostaArtistica

import unittest2 as unittest


class PropostaArtisticaIntegrationTest(unittest.TestCase):

    layer = PROPOSTA_ARTISTICA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='PropostaArtistica')
        schema = fti.lookupSchema()
        self.assertEqual(IPropostaArtistica, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='PropostaArtistica')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='PropostaArtistica')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IPropostaArtistica.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('PropostaArtistica', 'PropostaArtistica')
        self.assertTrue(
            IPropostaArtistica.providedBy(self.portal['PropostaArtistica'])
        )
