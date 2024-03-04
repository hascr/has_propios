# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class AccountMove(models.Model):
    _inherit = 'account.move'

    instructor = fields.Boolean(
        related='partner_id.instructor',
        string='Instructor'
    )
    aprobada = fields.Boolean(
        string='Pago aprobado'
    )
    


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(
        string='Instructor'
    )

    IBAN = fields.Char(
        string='Cuenta IBAN'
    )
