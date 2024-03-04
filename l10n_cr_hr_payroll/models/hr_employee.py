from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, AccessError
from odoo.osv import expression
from odoo.tools import format_date, Query


class HrEmployeePrivate(models.Model):
    """
    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.
    """
    _inherit = "hr.employee"

    children_to_report = fields.Integer(
        string='Number of children to report',
        groups="hr.group_hr_user",
        tracking=True
    )
    spouse_report = fields.Boolean(groups="hr.group_hr_user", tracking=True)
