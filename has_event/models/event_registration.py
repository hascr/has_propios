# -*- coding: utf-8 -*-

from odoo import models, fields, api


class has_eventregistration(models.Model):
    _inherit = 'event.registration'

    cedula = fields.Char(string='Cédula')
    placa = fields.Char(string='Placa')
    colaborador = fields.Char(string='N° Colaborador')
    correo = fields.Char(string='Correo personal')
    licencia = fields.Char(string='Licencia')
    asistencia = fields.Float (string='Horas asistidas')
    nota = fields.Float (string='Nota obtenida')
    asesor = fields.Many2one(comodel_name='res.users', tracking=True, string='Asesor')
    country_id = fields.Many2one(comodel_name='res.country', tracking=True, string='País')