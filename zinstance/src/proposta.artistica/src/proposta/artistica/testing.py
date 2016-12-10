# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import proposta.artistica


class PropostaArtisticaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=proposta.artistica)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'proposta.artistica:default')


PROPOSTA_ARTISTICA_FIXTURE = PropostaArtisticaLayer()


PROPOSTA_ARTISTICA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PROPOSTA_ARTISTICA_FIXTURE,),
    name='PropostaArtisticaLayer:IntegrationTesting'
)


PROPOSTA_ARTISTICA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PROPOSTA_ARTISTICA_FIXTURE,),
    name='PropostaArtisticaLayer:FunctionalTesting'
)


PROPOSTA_ARTISTICA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PROPOSTA_ARTISTICA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PropostaArtisticaLayer:AcceptanceTesting'
)
