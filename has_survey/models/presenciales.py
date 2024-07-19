# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class presenciales(models.Model):
    _name = 'presenciales'
    _auto = False
    _description = _('Presenciales')

    name = fields.Char(_('Participante'))
    fecha_evaluacion = fields.Datetime(_('Realizada el:'))
    nota = fields.Float(_('Nota total'), group_operator='avg')
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
    contenido = fields.Float(_('Contenido'), group_operator='avg')
    expectativa = fields.Float(_('Expectativa'), group_operator='avg')
    estructura = fields.Float(_('Estructura'), group_operator='avg')
    instructor_nota = fields.Float(_('Instrucción'), group_operator='avg')
    conocimiento = fields.Float(_('Conocimiento'), group_operator='avg')
    puntualidad = fields.Float(_('Puntualidad'), group_operator='avg')
    ejemplos = fields.Float(_('Uso de ejemplos'), group_operator='avg')
    dudas = fields.Float(_('Atención de dudas'), group_operator='avg')
    presentacion = fields.Float(_('Presentación personal'), group_operator='avg')
    otros = fields.Float(_('Otros aspectos'), group_operator='avg')
    material = fields.Float(_('Material de apoyo'), group_operator='avg')
    lugar = fields.Float(_('Condiciones de lugar'), group_operator='avg')
    maquinas = fields.Float(_('Desempeño de máquinas'), group_operator='avg')
    refrigerio = fields.Float(_('Refrigerio'), group_operator='avg')
    area_trabajo = fields.Char(_('Área de trabajo'))


    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW presenciales AS (
            SELECT		s.id AS id,
				s.end_datetime AS fecha_evaluacion,
				s.scoring_percentage AS nota,
				(	(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 54) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS expectativa
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 55) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS estructura
				) / 2 AS contenido,
				
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 54) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS expectativa,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 55) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS estructura,
				
				(	(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 57) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS conocimiento
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 58) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS puntualidad
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 62) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS ejemplos
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 60) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS dudas
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 75) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS presentacion
				) / 5 AS instructor_nota,
				
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 57) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS conocimiento,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 58) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS puntualidad,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 62) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS ejemplos,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 60) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS dudas,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 75) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS presentacion,
				
				
				(	(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 59) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS material
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 63) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS lugar
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 64) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS maquinas
					+
					(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 78) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 --AS refrigerio
				) / 4 AS Otros,
				
				
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 59) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS material,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 63) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS lugar,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 64) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS maquinas,
				(SELECT a.answer_score FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 78) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))*100 AS refrigerio,
				
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 65) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS enviar_info,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 51) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS curso,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 52) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS asesor,
				CASE WHEN (SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 69) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) IS NULL THEN (SELECT string_agg(SUBSTRING(a."value"->> 'es_CR', 1, LENGTH(a."value"->> 'es_CR') -0), ', ') AS answer_texts FROM survey_question_answer a WHERE a.id IN ( SELECT suggested_answer_id    FROM survey_user_input_line l    WHERE l.question_id = 69 AND l.user_input_id = s.id)) ELSE CONCAT((SELECT string_agg(SUBSTRING(a."value"->> 'es_CR', 1, LENGTH(a."value"->> 'es_CR') -0), ', ') AS answer_texts FROM survey_question_answer a WHERE a.id IN ( SELECT suggested_answer_id    FROM survey_user_input_line l    WHERE l.question_id = 69 AND l.user_input_id = s.id)),', ',(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 69) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) END AS intereses,
				(SELECT MAX(l.value_ans_sh_email) filter (WHERE l.question_id = 66) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS correo_intereses,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 71) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS name,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 72) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS empresa,
				CONCAT((SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 67) FROM	survey_user_input_line l WHERE l.user_input_id = s.id),(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 68) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS WhatsApp,
				(SELECT MAX(l.value_text_box) filter (WHERE l.question_id = 70) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS comentarios,
				(SELECT MAX(l.value_ans_sh_email) filter (WHERE l.question_id = 73) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS correo,
				(SELECT MAX(l.value_char_box) filter (WHERE l.question_id = 74) FROM	survey_user_input_line l WHERE l.user_input_id = s.id) AS telefono,
				(SELECT c.instructor FROM cursos c WHERE concat(c.codigo,' - ',c.curso) = (SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 51) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))) AS instructor,
				(SELECT c.sesiones * c.horassesion FROM cursos c WHERE concat(c.codigo,' - ',c.curso) = (SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 51) FROM	survey_user_input_line l WHERE l.user_input_id = s.id))) AS duracion,
				(SELECT a."value"->> 'es_CR' FROM survey_question_answer a WHERE a.id = (SELECT MAX(l.suggested_answer_id) filter (WHERE l.question_id = 114) FROM	survey_user_input_line l WHERE l.user_input_id = s.id)) AS area_trabjo

FROM			survey_user_input s

WHERE			s.STATE = 'done'
AND			s.survey_id = 4
                         );
            """)
        

    def go_to_presenciales(self):
        name_form = _('Presenciales')
        return {
        'name': name_form,
        'type': 'ir.actions.act_window',
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'survey.user_input',
        'res_id': self.id,  # Reference to the other model
        'target': 'current',
        'view_id': self.env.ref(
            'survey.survey_user_input_view_form').id,
        'context': {} # Optional
            }