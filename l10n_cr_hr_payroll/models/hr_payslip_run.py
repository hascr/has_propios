from odoo import _, api, fields, models, tools


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    ins_name = fields.Char()
    ins_file = fields.Binary(string="INS Report")
