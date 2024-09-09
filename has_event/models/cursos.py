# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class cursos(models.Model):
    _name = "cursos"
    _auto = False
    _description = "Vista de cursos"

    codigo = fields.Integer(string="Código")
    curso = fields.Char(string="Nombre de curso")
    instructor = fields.Char(string="Instructor")
    idinstructor = fields.Integer(string="idinstructor")
    inicio = fields.Datetime(string="Inicio")
    final = fields.Datetime(string="Final")
    fecha_aviso = fields.Datetime(string="Fecha aviso")
    matricula = fields.Char(string="Matricula")
    goto = fields.Char(string="Cuenta GoTo")
    sesiones = fields.Float(string="Sesiones")
    horassesion = fields.Float(string="Horas por sesión")
    horausd = fields.Float(string="Hora USD")
    enoficina = fields.Boolean(string="En Oficina")
    creacion = fields.Datetime(string="Creación")
    presencial = fields.Boolean(string="Presencial")
    noenviar = fields.Boolean(string="No bienvenida")
    urllearn = fields.Char(string="URL Learn")
    materiallearn = fields.Char(string="Material Learn")
    asesor = fields.Char(string="Asesor")
    actualizacion = fields.Char(string="Actualización")
    cedula_contrato = fields.Char(string="Cédula contrato")
    nombre_contrato = fields.Char(string="Nombre contrato")
    correo_contrato = fields.Char(string="Correo Contrato")
    cedula_facturacion_contrato = fields.Char(string="Cédula facturación contrato")
    nombre_facturacion_contrato = fields.Char(string="Nombre facturación contrato")
    nacionalidad_contrato = fields.Char(string="Nacionalidad contrato")
    nocontrato = fields.Boolean(string="Sin contrato")
    estado = fields.Integer(string="Estado")
    tipo = fields.Integer(string="Tipo")
    soporte = fields.Many2one(comodel_name="hr.employee", string="Soporte")
    correo_instructor = fields.Char(string="Correo instructor")

    def init(self):
        self._cr.execute(
            """
            CREATE OR REPLACE VIEW cursos AS (
            SELECT
 	ee.id AS id,
	ee.id AS codigo,
   ee.name ->> 'es_CR' AS curso,
   --(SELECT rp1.name FROM res_partner rp1 JOIN res_users ru1 on ru1.partner_id = rp1.id WHERE ru1.id = ee.asesor) AS vendedor,
   --(SELECT rp1.email FROM res_partner rp1 JOIN res_users ru1 on ru1.partner_id = rp1.id WHERE ru1.id = ee.asesor) AS correo,
   (SELECT rp1.name FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AS instructor,
   ee.instructor_id AS idinstructor,
   ee.date_begin AS inicio,
   ee.date_end AS final,
   date(ee.date_begin) AS fecha_aviso,
   ee.urlmatricula AS matricula,
	(SELECT ta.cuenta FROM training_account ta WHERE ta.id = ee.cuenta_id) AS goto,
-- ee.x_azurepass AS azurepass,
-- ee.x_labonline AS labonline,
   ee.cantsesion AS sesiones,
   ee.hsesion AS horassesion,
   ee.husd AS horausd,
   ee.enofi AS enoficina,
   ee.write_date AS creacion,
   ee.presencial AS presencial,
   ee.noenviar AS noenviar,
-- ee.learn AS learn,
   ee.urllearn AS urllearn,
   ee.materiallearn AS materiallearn,
	(SELECT rp1.email FROM res_partner rp1 JOIN res_users ru1 on ru1.partner_id = rp1.id WHERE ru1.id = ee.asesor) AS asesor,
	(to_char(ee.write_date, 'dd-mm-yyyy'::text) = to_char(now(), 'dd-mm-yyyy'::text)) AS actualizacion,
	(SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 2 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box' LIMIT 1) AS cedula_contrato,
	(SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 1 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box' LIMIT 1) AS nombre_contrato,
	(SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 7 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box' LIMIT 1) AS correo_contrato,
	(SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 5 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box' LIMIT 1) AS cedula_facturacion_contrato,
	(SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 4 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box' LIMIT 1) AS nombre_facturacion_contrato,
	CASE WHEN (SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 3 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box') IS NULL THEN 'Costarricense' ELSE (SELECT 	l.value_char_box FROM	survey_user_input_line l JOIN	survey_user_input i ON l.user_input_id = i.id WHERE	l.question_id = 3 AND	i.partner_id = (SELECT CASE WHEN rp1.parent_id IS NULL THEN rp1.id ELSE rp1.parent_id END FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AND	l.answer_type = 'char_box') END AS nacionalidad_contrato,
	ee.nocontrato AS nocontrato,
    ee.stage_id as estado,
    et."name" ->> 'es_CR' AS tipo,
    ee.soporte as soporte,
    (SELECT rp1.email FROM res_partner rp1 WHERE rp1.id = ee.instructor_id) AS correo_instructor

FROM event_event ee
LEFT JOIN res_users ru ON ru.id = ee.user_id
LEFT JOIN res_partner rp ON rp.id = ru.partner_id
LEFT JOIN event_type et ON ee.event_type_id = et.id
WHERE ee.stage_id != 5
                         );
            """
        )
