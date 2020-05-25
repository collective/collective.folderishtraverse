from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.folderishtraverse


class CollectiveFolderishtraverseLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.folderishtraverse)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.folderishtraverse:default")


COLLECTIVE_FOLDERISHTRAVERSE_FIXTURE = CollectiveFolderishtraverseLayer()


COLLECTIVE_FOLDERISHTRAVERSE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FOLDERISHTRAVERSE_FIXTURE,),
    name="CollectiveFolderishtraverseLayer:IntegrationTesting",
)


COLLECTIVE_FOLDERISHTRAVERSE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FOLDERISHTRAVERSE_FIXTURE,),
    name="CollectiveFolderishtraverseLayer:FunctionalTesting",
)
