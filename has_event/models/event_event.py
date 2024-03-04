# -*- coding: utf-8 -*-

from odoo import models, fields, api


class has_event(models.Model):
    _inherit = 'event.event'

    presencial = fields.Boolean(string='Presencial', tracking=True)
    noenviar = fields.Boolean(string='No enviar recordatorios', tracking=True)
    materiallearn = fields.Char(string='Material Learn', tracking=True)
    urllearn = fields.Char(string='URL Learn', tracking=True)
    urlmatricula = fields.Char(string='URL matrícula', tracking=True)
    fechas_teams_pres = fields.Char(string='Fechas (Teams o presencial)', tracking=True)
    cantsesion = fields.Float (string='Cantidad de sesiones', tracking=True)
    hsesion = fields.Float (string='Horas por sesión', tracking=True)
    husd = fields.Float (string='Hora USD', tracking=True)
    enofi = fields.Boolean(string='En Oficina', tracking=True)
    titulo = fields.Boolean(string='Título entregado', tracking=True)
    cuenta_id = fields.Many2one(comodel_name='training.account', tracking=True, string='Cuenta Training')
    instructor_id = fields.Many2one(comodel_name='res.partner', tracking=True, string='Instructor', domain=[('instructor', '=', True)],)
    #instructor_id = fields.Many2one(comodel_name='instructor.name', tracking=True, string='Instructor')
    asesor = fields.Many2one(comodel_name='res.users', tracking=True, string='Realizar evaluación', domain=lambda self: [("groups_id", "=", self.env.ref( "sales_team.group_sale_salesman" ).id)])
    facturado = fields.Boolean(string='Facturado', tracking=True)
    contrato_firmado = fields.Binary(attachment=True)
    