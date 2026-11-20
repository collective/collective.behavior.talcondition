"""Setup/installation tests for this package."""

from collective.behavior.talcondition.testing import IntegrationTestCase
from plone.base.utils import get_installer


class TestInstall(IntegrationTestCase):
    """Test installation of collective.behavior.talcondition into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.behavior.talcondition is installed with portal_quickinstaller."""
        self.assertTrue(
            self.installer.is_product_installed("collective.behavior.talcondition")
        )

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveBehaviorTalconditionLayer is registered."""
        from collective.behavior.talcondition.interfaces import (
            ICollectiveBehaviorTalconditionLayer,
        )
        from plone.browserlayer import utils

        self.assertIn(ICollectiveBehaviorTalconditionLayer, utils.registered_layers())


class TestUninstall(IntegrationTestCase):
    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("collective.behavior.talcondition")

    def test_uninstall(self):
        """Test if collective.behavior.talcondition is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("collective.behavior.talcondition")
        )
