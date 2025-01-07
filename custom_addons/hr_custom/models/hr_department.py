from odoo import models, fields, api

class HrDepartement(models.Model):
    _inherit = 'hr.department'

    average_score = fields.Float(string='Average Score', compute='_compute_average_score')

    @api.depends('member_ids.performance_score')
    def _compute_average_score(self):
        for department in self:
            total_score = 0
            employee_count = len(department.member_ids)
            if employee_count > 0:
                for employee in department.member_ids:
                    total_score += employee.performance_score  
                department.average_score = total_score / employee_count
            else:
                department.average_score = 0