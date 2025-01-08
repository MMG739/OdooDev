from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    experience_level = fields.Selection(
        [('beginner', 'Débutant'), ('intermediate', 'Intermédiaire'), ('expert', 'Expert')],
        string="Niveau d'expérience",
    )
    certification_ids = fields.One2many('hr.certification.employee', 'employee_id', string='Certifications')
    performance_score = fields.Float(string='Score de performance')

    def action_export_employee_report(self):
        return self.env.ref('hr_custom.employee_report_pdf').report_action(self)
