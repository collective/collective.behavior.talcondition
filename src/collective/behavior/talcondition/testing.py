"""Base module for unittesting."""

from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.testing import zope

import collective.behavior.talcondition
import unittest


class CollectiveBehaviorTalconditionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    products = ("collective.behavior.talcondition",)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        self.loadZCML(package=collective.behavior.talcondition, name="testing.zcml")
        for p in self.products:
            zope.installProduct(app, p)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Set default chain for plone.app.contenttypes
        wftool = portal["portal_workflow"]
        wftool.setDefaultChain("simple_publication_workflow")

        # Install into Plone
        applyProfile(portal, "collective.behavior.talcondition:testing")
        applyProfile(portal, "plone.app.contenttypes:plone-content")

        # Login and create some test content
        setRoles(portal, TEST_USER_ID, ["Manager"])
        login(portal, TEST_USER_NAME)
        api.content.create(container=portal, type="Folder", id="folder")

        # Commit so that the test browser sees these objects
        import transaction

        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        for p in reversed(self.products):
            zope.uninstallProduct(app, p)


FIXTURE = CollectiveBehaviorTalconditionLayer(name="FIXTURE")


INTEGRATION = IntegrationTesting(bases=(FIXTURE,), name="INTEGRATION")


FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,), name="FUNCTIONAL")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION

    def setUp(self):
        super().setUp()
        self.portal = self.layer["portal"]


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL
