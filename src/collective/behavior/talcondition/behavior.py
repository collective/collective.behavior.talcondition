# -*- coding: utf-8 -*-
import logging
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides
from zope.interface import implements
from collective.behavior.talcondition import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from Products.CMFCore.Expression import Expression, createExprContext
from Products.CMFCore.utils import getToolByName

WRONG_TAL_CONDITION = "The TAL expression '%s' for element at '%s' is wrong.  Original exception : %s"


class ITALCondition(model.Schema):

    tal_condition = schema.TextLine(
        title=_(u'TAL condition'),
        description=_(u'Enter a TAL expression that once evaluated will return True if content should be available. '
                      'Elements \'member\', \'context\' and \'portal\' are available for the expression.'),
        required=False,
        default=u'',
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

    def evaluate(self):
        res = True
        # Check condition
        tal_condition = self.context.tal_condition.strip()
        if tal_condition:
            portal = getToolByName(self.context, 'portal_url').getPortalObject()
            ctx = createExprContext(self.context.aq_inner.aq_parent,
                                    portal,
                                    self.context)
            ctx.setGlobal('member', getToolByName(self.context, 'portal_membership').getAuthenticatedMember())
            ctx.setGlobal('context', self.context)
            ctx.setGlobal('portal', portal)
            try:
                res = Expression(tal_condition)(ctx)
            except Exception, e:
                logger = logging.getLogger('collective.behavior.talcondition')
                logger.warn(WRONG_TAL_CONDITION % (self.context.tal_condition,
                                                   self.context.absolute_url(),
                                                   str(e)))
                res = False
        return res
