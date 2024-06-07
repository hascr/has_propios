# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class evaluaciones(models.Model):
    _name = 'evaluaciones'
    _auto = False
    _description = _('Virtuales')

    name = fields.Char(_('Participante'))
    fecha_evaluacion = fields.Datetime(_('Realizada'))
    nota = fields.Float(_('Nota'), group_operator='avg')
    enviar_info = fields.Char(_('Enviar Información'))
    curso = fields.Char(_('Curso'))
    asesor = fields.Char(_('Asesor'))
    intereses = fields.Char(_('Intereses'))
    correo_intereses = fields.Char(_('Correo Interés'))
    empresa = fields.Char(_('Empresa'))
    whatsapp = fields.Char(_('WhatsApp'))
    comentarios = fields.Text(_('Comentarios'))
    correo = fields.Char(_('Correo Contacto'))
    telefono = fields.Char(_('Teléfono Contacto'))
    instructor = fields.Char(_('Instructor'))
    duracion = fields.Float(_('Duración'), group_operator='avg')

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW evaluaciones AS (
            SELECT		s.id AS id,
				s.end_datetime AS fecha_evaluacion,
				s.scoring_percentage AS nota,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 41) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS enviar_info,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 27) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS curso,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 28) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS asesor,
				CASE WHEN (SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 45) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) IS NULL THEN (SELECT string_agg(SUBSTRING(a."value"->> 'es_CR', 1, LENGTH(a."value"->> 'es_CR') -0), ', ') AS answer_texts FROM survey_question_answer a WHERE a.id IN ( SELECT suggested_answer_id    FROM survey_user_input_line l    WHERE l.question_id = 45 AND l.user_input_id = s.id)) ELSE CONCAT((SELECT string_agg(SUBSTRING(a."value"->> 'es_CR', 1, LENGTH(a."value"->> 'es_CR') -0), ', ') AS answer_texts FROM survey_question_answer a WHERE a.id IN ( SELECT suggested_answer_id    FROM survey_user_input_line l    WHERE l.question_id = 45 AND l.user_input_id = s.id)),', ',(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 45) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) END AS intereses,
				(SELECT MAX(l.value_ans_sh_email) filter (WHERE l.question_id = 42) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS correo_intereses,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 47) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS name,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 48) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS empresa,
				CONCAT((SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 43) FROM	survey_user_input_line l WHERE l.user_input_id = s.id),(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 44) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS WhatsApp,
				(SELECT MAX(l.value_text_box) filter (WHERE l.question_id = 46) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS comentarios,
				(SELECT MAX(l.value_ans_sh_email) filter (WHERE l.question_id = 49) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS correo,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 50) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS telefono,
				(SELECT c.instructor FROM cursos c WHERE concat(c.codigo,' - ',c.curso) = (SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 27) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))) AS instructor,
				(SELECT c.sesiones * c.horassesion FROM cursos c WHERE concat(c.codigo,' - ',c.curso) = (SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 27) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))) AS duracion

FROM			survey_user_input s

WHERE			s.STATE = 'done'
AND			s.survey_id = 3
                         );
            """)
        
    def go_to_virtuales(self):
        name_form = _('Virtuales')
        return {
        'name': name_form,
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'survey.user_input',
        'res_id': self.id,  # Reference to the other model
        'target': 'new',
        'view_id': self.env.ref(
            'survey.survey_user_input_view_form').id,
        'context': {} # Optional
            }