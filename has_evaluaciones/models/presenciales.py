# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class virtuales(models.Model):
    _name = "presenciales"
    _description = _("Presenciales")

    name = fields.Char(_("Participante"))
    fecha_evaluacion = fields.Datetime(_("Fecha Realizada"))
    nota = fields.Float(_("Nota"), group_operator="avg")
    enviar_info = fields.Char(_("Enviar Información"))
    curso = fields.Many2one("event.event", string="Curso")
    asesor = fields.Many2one("res.users", string="Asesor")
    intereses = fields.Char(_("Intereses"))
    correo_intereses = fields.Char(_("Correo Interés"))
    empresa = fields.Char(_("Empresa"))
    whatsapp = fields.Char(_("WhatsApp"))
    comentarios = fields.Text(_("Comentarios"))
    correo = fields.Char(_("Correo Contacto"))
    telefono = fields.Char(_("Teléfono Contacto"))
    instructor = fields.Many2one("res.partner", string="Instructor")
    duracion = fields.Float(_("Duración"), group_operator="avg")
    contenido = fields.Float(_("Contenido"), group_operator="avg")
    expectativa = fields.Float(_("Expectativa"), group_operator="avg")
    estructura = fields.Float(_("Estructura"), group_operator="avg")
    instructor_nota = fields.Float(_("Instrucción"), group_operator="avg")
    conocimiento = fields.Float(_("Conocimiento"), group_operator="avg")
    puntualidad = fields.Float(_("Puntualidad"), group_operator="avg")
    ejemplos = fields.Float(_("Uso de ejemplos"), group_operator="avg")
    dudas = fields.Float(_("Atención de dudas"), group_operator="avg")
    presentacion = fields.Float(_("Presentación personal"), group_operator="avg")
    otros = fields.Float(_("Otros aspectos"), group_operator="avg")
    material = fields.Float(_("Material de apoyo"), group_operator="avg")
    lugar = fields.Float(_('Condiciones de lugar'), group_operator='avg')
    maquinas = fields.Float(_('Desempeño de máquinas'), group_operator='avg')
    refrigerio = fields.Float(_('Refrigerio'), group_operator='avg')
    area_trabajo = fields.Char(_("Área de trabajo"))