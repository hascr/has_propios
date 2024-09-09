# -*- coding: utf-8 -*-

from odoo import models, fields, api


class has_event(models.Model):
    _inherit = "event.event"

    presencial = fields.Boolean(
        string="Presencial",
        tracking=True,
        help="En oficina de Advance o instalaciones físicas del cliente",
    )
    noenviar = fields.Boolean(string="Sin bienvenida", tracking=True)
    nocontrato = fields.Boolean(string="Sin contrato", tracking=True)
    materiallearn = fields.Char(string="Material Learn", tracking=True)
    urllearn = fields.Char(string="URL Learn", tracking=True)
    urlmatricula = fields.Char(string="URL matrícula", tracking=True)
    fechas_teams_pres = fields.Char(string="Fechas (Teams o presencial)", tracking=True)
    cantsesion = fields.Float(string="Cantidad de sesiones", tracking=True)
    hsesion = fields.Float(string="Horas por sesión", tracking=True)
    husd = fields.Float(string="Hora USD", tracking=True)
    enofi = fields.Boolean(
        string="En Oficina", tracking=True, help="Exclusivamente en oficina de Advance"
    )
    titulo = fields.Boolean(string="Título entregado", tracking=True)
    cuenta_id = fields.Many2one(
        comodel_name="training.account", tracking=True, string="Cuenta Training"
    )
    instructor_id = fields.Many2one(
        comodel_name="res.partner",
        tracking=True,
        string="Instructor",
        domain=[("instructor", "=", True)],
    )
    soporte = fields.Many2one(
        comodel_name="hr.employee",
        tracking=True,
        string="Soporte",
        domain=[("department_id", "=", 1), ("parent_id", "!=", False)],
    )
    # asesor = fields.Many2one(comodel_name='hr.employee', tracking=True, string='Realizar evaluación', domain=[('department_id', '=', 2),('parent_id', '!=', False)])
    asesor = fields.Many2one(
        comodel_name="res.users",
        tracking=True,
        string="Realizar evaluación",
        domain=lambda self: [
            ("groups_id", "=", self.env.ref("sales_team.group_sale_salesman").id)
        ],
    )
    contrato_firmado = fields.Binary(attachment=True)
    contrato_name = fields.Char()
    account_move_id = fields.Many2one(
        "account.move",
        string="Factura de Proveedor",
        domain=[("instructor", "=", True)],
        tracking=True,
    )
    monto_contrato = fields.Float(
        string="Monto contrato", compute="_monto_contrato", tracking=True
    )
    total_horas = fields.Float(
        string="Total horas", compute="_total_horas", tracking=True
    )
    temario = fields.Binary(attachment=True, string="Temario")
    temario_name = fields.Char()
    grupo = fields.Selection(
        [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
        ]
    )
    tipo_certificado = fields.Selection(
        [
            ("aprovechamiento", "Aprovechamiento"),
            ("participacion", "Participación"),
        ],
        string="Tipo de certificado",
    )

    nombre_contrato = fields.Char(string="Nombre contrato", compute="_compute_nombre_contrato", store=True)

    def go_to_contratos(self):
        name_form = "Contratos"
        return {
            "name": name_form,
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "event.event",
            "res_id": self.id,  # Reference to the other model
            "target": "current",
            "view_id": self.env.ref("event.view_event_form").id,
            "context": {},  # Optional
        }

    @api.depends("cantsesion", "hsesion", "husd")
    def _monto_contrato(self):
        for record in self:
            record.monto_contrato = record.cantsesion * record.hsesion * record.husd

    @api.depends("cantsesion", "hsesion")
    def _total_horas(self):
        for record in self:
            record.total_horas = record.cantsesion * record.hsesion

    def solicitar_programacion(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/0AVpVrJjDZ",
        }

    def crear_programacion(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://form.jotform.com/232511329331042",
        }

    def videos_moodle(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/JYTswkjtqr",
        }

    def generar_titulos(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/9vjjdc9evX",
        }

    def enviar_titulos(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/eHGK9Mc61t",
        }

    def generar_asistencia(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/EDc3LbueEt",
        }

    def correo_bienvenida(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/wUdm1upyPW",
        }

    def enviar_contratos(self):
        return {
            "type": "ir.actions.act_url",
            "target": "new",
            "url": "https://forms.office.com/r/eDYaKh78fg",
        }
