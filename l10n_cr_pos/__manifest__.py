# -*- coding: utf-8 -*-
{
    'name': "Facturación Electronica Costa Rica",

    'summary': "Emisión de documentos electrónicos desde el punto de venta",

    'description': """
Long description of module's purpose
    """,

    'author': "Manexware SA",
    'website': "https://www.manexware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '17.0.1.0.1',
    "license": "AGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['cr_electronic_invoice', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_payment_method_views.xml',
        # 'views/report_invoice.xml',
        'views/ticket_validation_screen.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'l10n_cr_pos/static/src/**/*',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
