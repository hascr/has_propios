# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools

# from odoo.addons.base.models.res_currency import Currency


class AccountPaymentCertif(models.Model):
    _inherit = "account.payment"

    certificacion = fields.Binary(attachment=True)


class retenciones(models.Model):
    _name = "retenciones"
    _auto = False
    _description = "Reporte retenciones"

    payment_date = fields.Date(string="Fecha de pago")
    partner_id = fields.Many2one("res.partner", string="Cliente")
    user_id = fields.Many2one(
        "res.users",
        string="Asesor",
    )
    amount = fields.Float(string="Monto")
    number_invoice = fields.Char(string="Número de factura")

    certificacion = fields.Binary(attachment=True, store=True, string="Certificación")

    def init(self):
        self._cr.execute(
            """
            CREATE OR REPLACE VIEW retenciones AS (
            SELECT 	a.id AS id,
			        m.ref AS number_invoice,
			        m.date AS payment_date,
			        m.partner_id AS partner_id,
			        a.amount as amount,
			        (SELECT m1.invoice_user_id FROM account_move m1 WHERE m1.payment_reference = m.ref AND m1.move_type <> 'entry' AND m1.payment_state <> 'reversed' ) AS user_id
                    --a.certificacion as certificacion

	        FROM    account_payment a
	        JOIN	account_move m ON m.id = a.move_id
	        JOIN	account_journal j ON m.journal_id = j.id

	        WHERE	a.payment_type = 'inbound'
	        AND	    m.state = 'posted'
	        AND     a.is_internal_transfer = FALSE
	        AND     a.partner_type = 'customer'
	        AND     j."code" = 'RET2'
            );



                         """
        )

    def go_to_pagos_ret(self):
        name_form = "Pagos"
        return {
            "name": name_form,
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "account.payment",
            "res_id": self.id,  # Reference to the other model
            "target": "current",
            "view_id": self.env.ref("account.view_account_payment_form").id,
            "context": {},  # Optional
        }
