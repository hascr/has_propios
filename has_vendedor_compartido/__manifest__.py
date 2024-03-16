# -*- coding: utf-8 -*-
{
    'name': "HAS - Vendedor compartido",

    'summary': "Permite compartir pedidos a vendedores",

    #'description': """
#Long description of module's purpose
#    """,

    'author': "HAS",
    #'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #'category': 'Uncategorized',
    #'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/sale_order.xml',
    ],
    'application': True,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}

