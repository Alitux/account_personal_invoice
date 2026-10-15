# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


def _update_conflicting_rule(env):
    """
    This hook updates the domain of the 'account.account_move_see_all' rule
    to prevent it from conflicting with the 'Personal Invoices' rule.

    Since Odoo 16 the (post) init hooks receive an ``env`` instead of
    ``(cr, registry)``.
    """
    rule_to_update = env.ref('account.account_move_see_all', raise_if_not_found=False)

    if rule_to_update:
        # Odoo 19 uses 'move_type' (the old 'type' field no longer exists).
        new_domain = "[('move_type', 'not in', ('out_invoice', 'out_refund'))]"
        if rule_to_update.domain_force != new_domain:
            _logger.info("Updating domain for rule 'account.account_move_see_all' to resolve conflict.")
            rule_to_update.write({
                'domain_force': new_domain
            })
