# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    first_wage_tax = fields.Float(
        related="company_id.first_wage_tax",
        readonly=False
    )
    second_wage_tax = fields.Float(
        related="company_id.second_wage_tax",
        readonly=False
    )
    third_wage_tax = fields.Float(
        related="company_id.third_wage_tax",
        readonly=False
    )
    fourth_wage_tax = fields.Float(
        related="company_id.fourth_wage_tax",
        readonly=False
    )

    amount_children = fields.Float(
        related="company_id.amount_children",
        readonly=False
    )
    amount_spouse = fields.Float(
        related="company_id.amount_spouse",
        readonly=False
    )

    hr_rule_D001 = fields.Float(
        related="company_id.hr_rule_D001",
        readonly=False
    )
    hr_rule_D002 = fields.Float(
        related="company_id.hr_rule_D002",
        readonly=False
    )

    ins_number = fields.Char(
        string="Number",
        related="company_id.ins_number",
        readonly=False
    )
    ins_fax = fields.Char(
        string="Fax",
        related="company_id.ins_fax",
        readonly=False
    )
    ins_header = fields.Char(
        string="Header",
        related="company_id.ins_header",
        readonly=False
    )
    ins_email = fields.Char(
        string="Email",
        related="company_id.ins_email",
        readonly=False
    )
