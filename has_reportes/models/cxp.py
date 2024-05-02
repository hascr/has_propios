# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class cxp(models.Model):
    _name = 'cxp'
    _auto = False
    _description = 'Reporte de cuentas por pagar'

    proveedor = fields.Char(
        string='Proveedor'
    )
    cedula = fields.Char(
        string='Cédula'
    )
    moneda_factura = fields.Char(
        string='Moneda Factura'
    )
    banco = fields.Char(
        string='Banco'
    )
    cuenta = fields.Char(
        string='Cuenta'
    )
    moneda_cuenta = fields.Char(
        string='Moneda Cuenta'
    )
    factura = fields.Char(
        string='Factura'
    )
    fecha_factura = fields.Date(
        string='Fecha Factura'
    )
    fecha_pago = fields.Date(
        string='Fecha Pago'
    )
    saldo = fields.Float(
        string='Saldo'
    )
    
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW cxp AS (
            SELECT		a.id AS id,
				a.invoice_partner_display_name AS proveedor,
				r.vat AS cedula,
				(SELECT	c.name FROM res_currency c WHERE a.currency_id = c.id) AS moneda_factura,
				b.name AS banco,
				p.acc_number AS cuenta,
				(SELECT	c.name FROM res_currency c WHERE p.currency_id = c.id) AS moneda_cuenta,
				a.ref AS factura,
				a.invoice_date AS fecha_factura,
				a.fecha_arreglo AS fecha_pago,
				CASE WHEN a.amount_residual !=0 THEN a.amount_residual ELSE a.amount_total END AS Saldo

FROM			account_move a
JOIN			res_partner r ON a.partner_id = r.id
LEFT JOIN	res_partner_bank p ON r.id = p.partner_id
LEFT JOIN	res_bank b ON p.bank_id = b.id

WHERE			a.move_type IN ('in_invoice','in_refund')
AND 			a.state IN ('posted')
AND			a.payment_state NOT IN ('paid'))
                         ;
            """)