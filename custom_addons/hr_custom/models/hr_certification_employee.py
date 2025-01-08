from odoo import models, fields, api

class HrCertificationEmployee(models.Model):
    _name = 'hr.certification.employee'
    _description = 'Certification Employee'

    certification_id = fields.Many2one('hr.certification', string='Certification', required=True, ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')
    date_obtention = fields.Date('Date Obtention', required=True)