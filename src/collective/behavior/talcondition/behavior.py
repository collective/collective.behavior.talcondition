# -*- coding: utf-8 -*-
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides
from zope.interface import implements
from collective.behavior.talcondition import _
from collective.behavior.talcondition.utils import evaluateExpressionFor
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model


class ITALCondition(model.Schema):

    tal_condition = schema.TextLine(
        title=_(u'TAL condition'),
        description=_(u'Enter a TAL expression that once evaluated will return True if content should be available. '
                      'Elements \'member\', \'context\' and \'portal\' are available for the expression.'),
        required=False,
        default=u'',
    )

    role_bypassing_talcondition = schema.Set(
        title=_(u''),
        description=_(u'Choose the differents roles who can bypass the tal condition.'),
        required=False,
        value_type=schema.Choice(vocabulary='plone.app.vocabularies.Roles'),
    )

    def evaluate(self):
        """Evaluate the condition and returns True or False."""

alsoProvides(ITALCondition, IFormFieldProvider)


class TALCondition(object):
    """
    """

    implements(ITALCondition)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context

    def get_tal_condition(self):
        return getattr(self.context, 'tal_condition', '')

    def set_tal_condition(self, value):
        self.context.tal_condition = value

    tal_condition = property(get_tal_condition, set_tal_condition)

    def get_role_bypassing_talcondition(self):
        return getattr(self.context, 'role_bypassing_talcondition', '')

    def set_role_bypassing_talcondition(self, value):
        self.context.role_bypassing_talcondition = value

    role_bypassing_talcondition = property(get_role_bypassing_talcondition, set_role_bypassing_talcondition)

    def evaluate(self):
        return evaluateExpressionFor(self)
