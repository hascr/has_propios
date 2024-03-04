# -*- coding: utf-8 -*-
{
    'name': "HAS - Cambio de textos - PA",

    'summary': """
        Cambios de textos en módulos de Panamá""",

    #'description': """
    #    Long description of module's purpose
    #""",

    'author': "HAS",
    'license': 'LGPL-3',
    #'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #'category': 'Uncategorized',
    #'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','event','hr'],

    # always loaded
    'data': [
        'views/res_partner_view.xml',
        'views/crm_lead_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'application': True,
}
