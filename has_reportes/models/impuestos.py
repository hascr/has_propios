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
        string='Nombre Impuesto'
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
            SELECT	a.id AS ID,
			n.code AS codigo_cuenta,
			n.name->>'es_CR' AS cuenta,
			CASE WHEN r.name IS NULL THEN 'No definido' ELSE r.name END AS empresa,
			CASE WHEN t.name->>'es_CR' IS NULL THEN 'No definido' ELSE t.name->>'es_CR' END AS impuesto,
			-a.balance AS base_impuesto,
			CASE WHEN t.type_tax_use = 'purchase' THEN 'compra' ELSE	CASE WHEN t.type_tax_use = 'sale' THEN 'venta' ELSE 'manual' END END AS tipo,
			a.ref AS factura,
			a.date AS fecha,
			ROUND(-a.balance * t.amount / 100,2) AS saldo
			
			


FROM				account_move_line a
LEFT JOIN		account_move_line_account_tax_rel l ON a.id = l.account_move_line_id
LEFT JOIN		account_tax t ON l.account_tax_id = t.id
LEFT JOIN		res_partner r ON a.partner_id = r.id
LEFT JOIN		account_account n ON a.account_id = n.id

WHERE				a.parent_state = 'posted'
AND				t.name->>'es_CR' IS NOT NULL
                         )
                         ;
            """)