from odoo import fields, models


class HrContract(models.Model):
    """
    Employee contract based on the visa, work permits
    allows to configure different Salary structure
    """

    _inherit = "hr.contract"

    christmas_savings = fields.Monetary(groups="hr.group_hr_user", tracking=True)
    school_salary = fields.Float(groups="hr.group_hr_user", tracking=True)
