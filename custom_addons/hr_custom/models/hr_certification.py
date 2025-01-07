from odoo import models, fields

class HrCertification(models.Model):
    _name = 'hr.certification'
    _description = 'Certification des employés'

    name = fields.Char(string='Nom de la certification', required=True)
    description = fields.Text(string='Description')
    date_obtention = fields.Date(string='Date d\'obtention')
    employee_ids = fields.Many2many('hr.employee', string='Employés')