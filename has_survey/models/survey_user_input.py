# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Survey_user_input(models.Model):
    _inherit = 'survey.user_input'

    asesor = fields.Char(string='Asesor')
    correo_asesor = fields.Char(string='Correo Asesor', compute='_compute_asesor_correo', store=True)


    @api.depends('survey_id', 'state')
    def _compute_asesor(self):
        for record in self:
            if record.state == 'done' and record.survey_id.id == 7:
                self.env.cr.execute("""
                    SELECT (SELECT a."value"->> 'es_CR' 
                            FROM survey_question_answer a 
                            WHERE a.id = (SELECT MAX(l.suggested_answer_id) 
                                        filter (WHERE l.question_id = 125) 
                                        FROM survey_user_input_line l 
                                        WHERE l.user_input_id = %s)) AS asesor
                """, (record.id,))
                record.asesor = self.env.cr.fetchone()[0] if self.env.cr.rowcount > 0 else ''

    @api.depends('asesor')
    def _compute_asesor_correo(self):
            for record in self:
                correo = self.env['res.partner'].search([('name', '=', record.asesor)])
            if correo:
                record.correo_asesor = correo.email
            else:
                record.correo_asesor = 'jocampo@adltcr.com'  # Set asesor to None if no match
