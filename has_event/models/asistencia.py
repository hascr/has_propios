# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class asistencia(models.Model):
    _name = 'asistencia'
    _description = _('Asistencia de sesiones de entrenamiento')
    _rec_name = 'nombre'

    codigo = fields.Char(string="Código")
    nombre = fields.Char(string="Nombre completo")
    correo = fields.Char(string="Correo electrónico")
    curso = fields.Char(string="Curso")
    cuenta = fields.Char(string="Cuenta")
    fecha = fields.Datetime(string="Fecha")
    minutos = fields.Float(string="Minutos conectados")
    tipo = fields.Char(string="Tipo")
    duplicados = fields.Char(string="revisar duplicados")
    _sql_constraints = [('duplicados_unique', 'unique(duplicados)', "El códdigo duplicados debe ser único")]