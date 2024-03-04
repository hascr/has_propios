
from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    first_wage_tax = fields.Float()
    second_wage_tax = fields.Float()
    third_wage_tax = fields.Float()
    fourth_wage_tax = fields.Float()

    amount_children = fields.Float()
    amount_spouse = fields.Float()

    hr_rule_D001 = fields.Float()
    hr_rule_D002 = fields.Float()

    ins_number = fields.Char()
    ins_fax = fields.Char()
    ins_header = fields.Char()
    ins_email = fields.Char()