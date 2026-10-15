# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


# Odoo 19 uses 'move_type' (the old 'type' field no longer exists).
NEW_DOMAIN = "[('move_type', 'not in', ('out_invoice', 'out_refund'))]"

# Core account rules that grant blanket access to every journal entry (and
# therefore to every invoice/refund). They conflict with the "only my
# invoices" rule, so their domain is narrowed so they no longer cover
# customer invoices/refunds.
CONFLICTING_RULES = (
    # group "Invoicing"
    'account.account_move_see_all',
    # group "Invoicing" (readonly variant)
    'account.account_move_rule_group_invoice',
)


def _update_conflicting_rule(env):
    """
    Narrow the domain of the core account rules that would otherwise let the
    "Invoicing" group read every invoice, so that only the 'Personal Invoices'
    rule governs who can see customer invoices/refunds.

    Since Odoo 16 the (post) init hooks receive an ``env`` instead of
    ``(cr, registry)``.
    """
    for xmlid in CONFLICTING_RULES:
        rule = env.ref(xmlid, raise_if_not_found=False)
        if rule and rule.domain_force != NEW_DOMAIN:
            _logger.info("Updating domain of rule '%s' to resolve conflict.", xmlid)
            rule.write({'domain_force': NEW_DOMAIN})
