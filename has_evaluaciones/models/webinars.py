# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class virtuales(models.Model):
    _name = "webinars"
    _description = _("Webinars")

    fecha_evaluacion = fields.Datetime(_("Fecha Realizada"))
    nota = fields.Float(_("Nota"), group_operator="avg")
    enviar_info = fields.Char(_("Enviar Información"))
    curso = fields.Many2one("event.event", string="Curso")
    fuente = fields.Char(_('Fuente'))
    intereses = fields.Char(_("Intereses"))
    correo_intereses = fields.Char(_("Correo Interés"))
    whatsapp = fields.Char(_("WhatsApp"))
    comentarios = fields.Text(_("Comentarios"))
    correo = fields.Char(_("Correo Contacto"))
    instructor = fields.Many2one("res.partner", string="Instructor")
    temas_actualizados = fields.Float(_('Temas actualizados'), group_operator='avg')
    temas_utiles = fields.Float(_('Temas útiles'), group_operator='avg')
    estructura = fields.Float(_('Estructura'), group_operator='avg')
    conocimiento = fields.Float(_('Conocimiento'), group_operator='avg')
    rendimiento = fields.Float(_('Rendimiento'), group_operator='avg')
    area_trabajo = fields.Char(_('Área de trabajo'))