# -*- coding: utf-8 -*-
{
    'name': "HAS - Área de trabajo",

    'summary': "Agrega campos de trabajo a varios modelos",

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
    'depends': ['base','crm','event','has_event'],

    # always loaded
    'data': [
        'data/area_trabajo.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/res_partner.xml',
        'views/crm_lead.xml',
        'views/mailing_contact.xml',
        'views/event_registration.xml',
    ],
    'application': True,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}

