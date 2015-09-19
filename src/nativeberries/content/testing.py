# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import nativeberries.content


class NativeberriesContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=nativeberries.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nativeberries.content:default')


NATIVEBERRIES_CONTENT_FIXTURE = NativeberriesContentLayer()


NATIVEBERRIES_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NATIVEBERRIES_CONTENT_FIXTURE,),
    name='NativeberriesContentLayer:IntegrationTesting'
)


NATIVEBERRIES_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NATIVEBERRIES_CONTENT_FIXTURE,),
    name='NativeberriesContentLayer:FunctionalTesting'
)


NATIVEBERRIES_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NATIVEBERRIES_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='NativeberriesContentLayer:AcceptanceTesting'
)
