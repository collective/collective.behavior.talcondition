# -*- coding: utf-8 -*-
from zope.component import adapts

from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField


from Products.Archetypes.public import StringWidget, StringField
from Products.Archetypes.public import LinesField, MultiSelectionWidget

from collective.behavior.talcondition.interfaces import ITALConditionable
from collective.behavior.talcondition.interfaces import ICollectiveBehaviorTalconditionLayer


class TALConditionStringField(ExtensionField, StringField):
    """A string field that will contain an eventual TAL condition expression."""


class TALConditionLinesField(ExtensionField, LinesField):
    """A Lines field that will contain all roles who can bypass tal condition."""


class TALConditionExtender(object):
    """TALCondition class"""

    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    # adapts elements that provide the IExternalIdentifierable marker interface
    adapts(ITALConditionable)

    layer = ICollectiveBehaviorTalconditionLayer

    fields = [
        TALConditionStringField(
            'tal_condition',
            required=False,
            default='',
            searchable=False,
            languageIndependent=True,
            widget=StringWidget(
                label=(u"TAL condition expression"),
                description=(u'Enter a TAL expression that once evaluated will return True '
                             'if content should be available. '
                             'Elements \'member\', \'context\' and \'portal\' are available for the expression.'),)),

        TALConditionLinesField(
            'role_bypassing_talcondition',
            required=False,
            searchable=False,
            languageIndependent=True,
            widget=MultiSelectionWidget(
                size=10,
                label=(u"Role who can bypass TAL condition"),
                description=(u'Choose the differents roles who can bypass the tal condition.'),),
            enforceVocabulary=True,
            multiValued=1,
            vocabulary_factory='plone.app.vocabularies.Roles',),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
