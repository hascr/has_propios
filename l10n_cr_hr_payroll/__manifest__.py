# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Costa Rica Payroll",
    "version": "17.0.1.0.1",
    "category": "Human Resources/Expenses",
    "sequence": 16,
    "author": "Odoo CR Team",
    "website": "https://github.com/odoocr/l10n_cr_priv",
    "depends": ["hr", "om_hr_payroll"],
    "data": [
        "data/hr_salary_rule_category.xml",
        "data/hr_salary_rule_data.xml",
        "data/hr_payroll_structure_data.xml",
        "data/hr_holidays_data.xml",
        "views/hr_employee.xml",
        "views/hr_contract_views.xml",
        "views/hr_payslip_run_views.xml",
        "views/res_config_settings_views.xml",
        "wizard/hr_payroll_payslips_by_employees_views.xml",
        "views/hr_leave_views.xml",
        "security/ir.model.access.csv"
    ],
    "demo": [],
    "test": [],
    "auto_install": False,
    "application": True,
    "license": "AGPL-3",
    "assets": {},
}
