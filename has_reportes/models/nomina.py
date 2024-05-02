# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class nomina(models.Model):
    _name = 'nomina'
    _auto = False
    _description = 'Reporte de nómina'

    fecha = fields.Date(
        string='Fecha'
    )
    identificador = fields.Char(
        string='Identificador'
    )
    nombre = fields.Char(
        string='Nombre'
    )
    moneda = fields.Char(
        string='Moneda'
    )
    salario_crc = fields.Float(
        string='Salario CRC'
    )
    salario_usd = fields.Float(
        string='Salario USD'
    )
    salario_colonizado = fields.Float(
        string='Salario colonizado'
    )
    retencion_salario = fields.Float(
        string='Retención salario'
    )
    

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW nomina AS (
            SELECT		P.id AS id,
				date(PR.date_end) AS fecha,
    			concat(0,E.identification_id) AS identificador,
    			UPPER(E.name) AS nombre,
    			(SELECT c.name FROM res_currency c WHERE P.currency_id = c.id) AS moneda,
    			SUM(CASE WHEN PL.code = 'GROSS' AND PL.currency_id != 1 THEN PL.amount ELSE NULL END) AS salario_crc,
				SUM(CASE WHEN PL.code = 'GROSS' AND PL.currency_id = 1 THEN PL.amount ELSE NULL END) AS salario_usd, 
				ROUND(CAST(SUM(CASE
            		WHEN PL.code = 'GROSS' AND PL.currency_id != 1 THEN PL.amount
            		WHEN PL.code = 'GROSS' AND PL.currency_id = 1 THEN PL.amount * P.original_rate
            	ELSE 0 END) AS NUMERIC),2) AS salario_colonizado,
    			ROUND(CAST(SUM(CASE WHEN PL.code = 'RETSAL' OR PL.code = 'RETSALUSD' THEN PL.amount * P.original_rate ELSE 0 END) AS NUMERIC),2) AS retencion_salario
FROM 			hr_payslip_line PL
    JOIN 	Hr_employee E ON PL.employee_id = E.id
    JOIN 	hr_payslip P ON P.id = PL.slip_id
    JOIN 	hr_payslip_run PR ON PR.id = P.payslip_run_id
GROUP BY 	P.id, FECHA, IDENTIFICADOR, NOMBRE, MONEDA
ORDER BY 1);
            """)