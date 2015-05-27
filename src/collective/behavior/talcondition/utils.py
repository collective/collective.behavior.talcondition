# -*- coding: utf-8 -*-
import logging
from Products.CMFCore.Expression import Expression, createExprContext
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger('collective.behavior.talcondition')
WRONG_TAL_CONDITION = "The TAL expression '%s' for element at '%s' is wrong.  Original exception : %s"


def evaluateExpressionFor(obj, bypass_for_manager=False):
    """Evaluate the expression stored in 'tal_condition' of given p_obj.
    """
    res = True

    # Check condition
    tal_condition = obj.tal_condition and obj.tal_condition.strip() or ''
    if hasattr(obj, 'context'):
        obj = obj.context

    member = getToolByName(obj, 'portal_membership').getAuthenticatedMember()
    if bypass_for_manager and member.has_role('Manager', obj):
        return res

    if tal_condition:
        portal = getToolByName(obj, 'portal_url').getPortalObject()
        ctx = createExprContext(obj.aq_inner.aq_parent,
                                portal,
                                obj)
        ctx.setGlobal('member', member)
        ctx.setGlobal('context', obj)
        ctx.setGlobal('portal', portal)
        try:
            res = Expression(tal_condition)(ctx)
        except Exception, e:
            logger.warn(WRONG_TAL_CONDITION % (obj.tal_condition,
                                               obj.absolute_url(),
                                               str(e)))
            res = False
    return res


def applyExtender(portal, meta_types):
    """
      We add a 'tal_condition' field using archetypes.schemaextender
      to every given p_meta_types.
    """
    logger.info("Adding field 'tal_condition' : updating the schema for meta_types %s" % ','.join(meta_types))
    at_tool = getToolByName(portal, 'archetype_tool')
    catalog = getToolByName(portal, 'portal_catalog')
    catalog.ZopeFindAndApply(portal,
                             obj_metatypes=meta_types,
                             search_sub=True,
                             apply_func=at_tool._updateObject)
    logger.info("Done!")
