# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class movimientobancario(models.Model):
    _name = 'movimiento.bancario'
    _auto = False
    _description = 'Reporte de Movimiento de cuentas bancario'

    cuenta = fields.Char(
        string='Cuenta'
    )
    codigo = fields.Char(
        string='Código'
    )
    moneda_cuenta = fields.Char(
        string='Moneda Cuenta'
    )
    empresa = fields.Char(
        string='Empresa'
    )
    factura = fields.Char(
        string='Factura'
    )
    descripcion = fields.Char(
        string='Descripción'
    )
    fecha = fields.Date(
        string='Fecha'
    )
    saldo = fields.Float(
        string='Saldo'
    )
    estado = fields.Char(
        string='Estado'
    )
    
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW movimiento_bancario AS (
            SELECT		a.id AS id,
				c.name->>'es_CR' AS cuenta,
				c.code AS codigo,
				(SELECT	y.name FROM res_currency y WHERE a.currency_id = y.id) AS moneda_cuenta,
				r.name AS empresa,
				--t.name->>'es_CR' AS impuesto,
				--a.tax_base_amount AS base_impuesto,
				--t.type_tax_use AS tipo_impuesto,
				a.ref AS factura,
				a.name AS descripcion,
				a.date AS fecha,
				--a.balance saldo,
				--a.amount_currency AS saldo_usd,
				CASE WHEN (SELECT	y.name FROM res_currency y WHERE a.currency_id = y.id) = 'CRC' THEN a.balance ELSE a.amount_currency END AS saldo,
				a.parent_state AS estado
				
FROM			account_move_line a
LEFT JOIN	account_account c ON a.account_id = c.id
LEFT JOIN	res_partner r ON a.partner_id = r.id
LEFT JOIN	account_tax t ON a.tax_line_id = t.id
LEFT JOIN	account_group g ON c.group_id = g.id

WHERE			(g.code_prefix_start LIKE '1101%' OR g.code_prefix_start LIKE '1102%')
AND			c.code NOT LIKE '11010199')
                         ;
            """)