# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class contactos_duplicados(models.Model):
    _name = 'contactos.duplicados'
    _auto = False
    _description = 'Reporte de contactos duplicados'
    _rec_name = 'contacto'

    creacion = fields.Datetime(
        string="Fecha creación")
        
    contacto = fields.Char(
        string='Contacto')

    empresa = fields.Char(
        string='Empresa')
    
    email = fields.Char(
        string='Correo electrónico')
    
    cedula = fields.Char(
        string='Cédula')
    
    telefono = fields.Char(
        string='Teléfono')
    
    asesor = fields.Char(
        string='Asesor')
        
    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW contactos_duplicados AS (
            SELECT	r.id AS id,
			r.create_date AS creacion,
			r.name AS contacto,
			r.commercial_company_name AS empresa,
			r.email_normalized AS email,
--			r.parent_id AS parent,
--			r.complete_name AS nombre_completo,
			r.vat AS cedula,
			r.phone_sanitized AS telefono,
			(SELECt rp1.name FROM res_partner rp1 WHERE rp1.id = (SELECT r1.partner_id FROM res_users r1 WHERE r.user_id = r1.id)) AS asesor
--			r.is_company AS es_empresa
			

FROM		res_partner r

WHERE		r.email_normalized IN (SELECT LOWER(r.email_normalized) AS correo FROM res_partner r GROUP BY correo HAVING COUNT(r.email_normalized) > 1)

ORDER BY	r.email_normalized ASC
                         )
                         ;
            """)
    
    def go_to_contactos(self):
        name_form = _('Contactos')
        return {
        'name': name_form,
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'res.partner',
        'res_id': self.id,  # Reference to the other model
        'target': 'current',
        'view_id': self.env.ref(
            'base.view_partner_form').id,
        'context': {} # Optional
            }