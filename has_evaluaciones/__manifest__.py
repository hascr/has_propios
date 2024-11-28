# -*- coding: utf-8 -*-
{
    'name': 'HAS - Evaluaciones',
    #'version': '1.0.0',
    'description': """ Agregar vista de evaluaciones """,
    'summary': """ Agregar vista de evaluaciones """,
    'author': 'HAS',
    'website': '',
    'category': '',
    'depends': ['base','survey'],
    "data": [
        "views/virtuales_views.xml",
        "security/ir.model.access.csv",
        "views/presenciales_views.xml",
        "views/webinars_views.xml"
    ],
    'application': True,
    #'installable': True,
    #'auto_install': False,
    'license': 'LGPL-3',
}
