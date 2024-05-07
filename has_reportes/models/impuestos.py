# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class reporte_impuestos(models.Model):
    _name = 'reporte.impuestos'
    _auto = False
    _description = 'Reporte de movimiento de impuestos'

    codigo_cuenta = fields.Char(
        string='Código'
    )
    cuenta = fields.Char(
        string='Cuenta'
    )
    empresa = fields.Char(
        string='Empresa'
    )
    impuesto = fields.Char(
        string='Impuesto'
    )
    base_impuesto = fields.Float(
        string='Monto base'
    )
    tipo = fields.Char(
        string='Tipo'
    )
    factura = fields.Char(
        string='Factura'
    )
    fecha = fields.Date(
        string='Fecha'
    )
    saldo = fields.Float(
        string='Impuesto'
    )
        
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW reporte_impuestos AS (
            SELECT		a.id AS id,
				c.code AS codigo_cuenta,
				c.name->>'es_CR' AS cuenta,
--				(SELECT	y.name FROM res_currency y WHERE a.currency_id = y.id) AS moneda_cuenta,
--				a.balance / (t.amount/100) AS base,
				CASE WHEN r.name IS NULL THEN 'No definido' ELSE r.name END AS empresa,
				CASE WHEN t.name->>'es_CR' IS NULL THEN 'No definido' ELSE t.name->>'es_CR' END AS impuesto,
				CASE WHEN -a.balance < 0 THEN CASE WHEN a.tax_base_amount IS NULL THEN 0 ELSE -a.tax_base_amount END ELSE CASE WHEN a.tax_base_amount IS NULL THEN 0 ELSE a.tax_base_amount END END AS base_impuesto,
--				t.type_tax_use AS tipo_impuesto,
				CASE WHEN t.type_tax_use = 'purchase' THEN 'compra' ELSE	CASE WHEN t.type_tax_use = 'sale' THEN 'venta' ELSE 'manual' END END AS tipo,
				a.ref AS factura,
--				a.name AS descripcion,
				a.date AS fecha,
				-a.balance saldo
--				a.amount_currency AS saldo_usd,
--				CASE WHEN (SELECT	y.name FROM res_currency y WHERE a.currency_id = y.id) = 'CRC' THEN a.balance ELSE a.amount_currency END AS saldo
--				a.parent_state AS estado
				
FROM			account_move_line a
LEFT JOIN	account_account c ON a.account_id = c.id
LEFT JOIN	res_partner r ON a.partner_id = r.id
LEFT JOIN	account_tax t ON a.tax_line_id = t.id
LEFT JOIN	account_group g ON c.group_id = g.id

WHERE			(g.code_prefix_start LIKE '1106%' OR g.code_prefix_start LIKE '2103%')
AND			a.parent_state = 'posted'
                         )
                         ;
            """)