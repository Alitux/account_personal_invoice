# -*- coding: utf-8 -*-
{
    'name': "Account Personal Invoices",

    'summary': "Show/validate only invoices of the current user with Ad-Hoc Argentina Localization",

    'description': """
        Show only invoices of the current user.
        This module add a new group "Personal Invoices" that is used to filter invoices.
    """,

    'author': "Alitux",
    'website': "https://www.alitux.com.ar",

    'category': 'Accounting',
    'version': '0.1',

    'depends': ['base', 'account','l10n_ar_afipws_fe'],

    'data': [
        'security/ir_model.access.xml',
        'security/account_security.xml',
        'security/ir_rules.xml',
        'views/view_move_form.xml',
    ],
}

