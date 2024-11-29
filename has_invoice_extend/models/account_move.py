# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class AccountMove(models.Model):
    _inherit = "account.move"

    instructor = fields.Boolean(related="partner_id.instructor", string="Instructor")
    """ aprobada = fields.Boolean(
        string='Pago aprobado'
    ) """
    fecha_arreglo = fields.Date(string="Fecha programada de pago")
    validado = fields.Boolean(string="Validado Hacienda")


class ResPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean(string="Instructor")

    """ IBAN = fields.Char(
        string='Cuenta IBAN'
    ) """

    gobierno = fields.Boolean(string="¿Gobierno?")

    is_factura_recordatorio = fields.Boolean(string='No enviar recordatorio', default=False, help='No enviar recordatorio cuando se encuentre la factura pendiente')
