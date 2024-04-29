# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class account_payment(models.Model):
    _inherit = "account.payment"
    
    # def post(self):
    #     res = super(account_payment, self).post()
    #     if self.partner_type == 'supplier' and self.partner_id.parent_id.custom_allow_send_mail or self.partner_id.custom_allow_send_mail:
    #         template = self.env.ref('account.mail_template_data_payment_receipt', False)
    #         template.send_mail(self.id)
    #     return res

    def action_post(self):
        res = super(account_payment, self).action_post()
        if self.partner_type == 'supplier' and self.partner_id.parent_id.custom_allow_send_mail or self.partner_id.custom_allow_send_mail:
            template = self.env.ref('payment_report_send_by_mail.mail_template_data_payment_receipt_supplier', False)
            print(template)
            template.send_mail(self.id)
        return res
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
