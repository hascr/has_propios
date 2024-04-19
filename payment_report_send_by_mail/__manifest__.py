# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payment Receipt Send by Mail Automatically',
    'version': '5.1.2',
    'category': 'Invoices & Payments',
    'price': 13.0,
    'currency': 'EUR',
    'summary': """Automatically send payment receipt/report to supplier.""",
    'description': """
Payment Receipt Send by Mail Automatically
Payment Receipt Send by Mail
customer payment receipt
customer receipt send by email
customer receipt
customer payment report
payment report send
send payment receipt

    """,
    'license': 'LGPL-3',
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/payment_report_send_by_mail/1047',#'https://youtu.be/GNOdhEZyo6A',
    'images': ['static/description/image.png'],
    'support': 'contact@probuse.com',
    'depends': ['account'],
    'data': [
        'views/res_partner.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
