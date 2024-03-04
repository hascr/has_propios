# -*- coding: utf-8 -*-
{
    'name': "HAS - Control de cursos",

    'summary': """
        Cambios en módulo base event_event""",

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
    'depends': ['base','event','hr'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/event_event.xml",
        "views/training_accounts.xml",
        "views/instructor_name.xml",
        "views/event_registration.xml",
        "views/event_registration_combine.xml",
        "views/programacion_views.xml",
        "security/ir.model.access.csv",
        "views/programacion_views.xml",
        "views/cursos_views.xml",
        "security/ir.model.access.csv",
        "views/estudiantes_views.xml",
        "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'application': True,
}
