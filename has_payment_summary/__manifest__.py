# -*- coding: utf-8 -*-

{
    'name': 'HAS - Cobros y comisiones',
    'author': "HAS",
    'license': 'LGPL-3',
    'summary': 'Cobros de clientes y comisiones',
    'depends': [
        'account',
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/payment_summary_views.xml',
        'views/menu.xml',
    ],
    'application': True,
}
