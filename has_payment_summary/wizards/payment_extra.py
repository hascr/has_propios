# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Sitaram Solutions (<https://sitaramsolutions.in/>).
#
#    For Module Support : info@sitaramsolutions.in  or Skype : contact.hiren1188
#
##############################################################################

from odoo import fields, models


class srAccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'
    
    journal_type = fields.Selection(related='journal_id.type')
    material = fields.Monetary(string="Material")
    consultoria = fields.Boolean(string="Consultoria")

    def _create_payment_vals_from_wizard(self, batch_result):
        payment_vals = super(srAccountPaymentRegister,self)._create_payment_vals_from_wizard(batch_result)
        if payment_vals:
            payment_vals.update({'material': self.material})
        return payment_vals

