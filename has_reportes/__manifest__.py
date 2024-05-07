# -*- coding: utf-8 -*-

{
    'name': 'HAS - Reportes',
    'author': "HAS",
    'license': 'LGPL-3',
    'summary': 'Reportes de varios módulos',
    'depends': [
        'account',
        'base'
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/nomina.xml",
        "views/cxp_views.xml",
        "views/movimiento_bancario_views.xml",
        "views/reporte_impuestos_views.xml"
    ],
    'application': True,
}
