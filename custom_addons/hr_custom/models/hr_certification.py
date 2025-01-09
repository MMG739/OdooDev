from odoo import models, fields, api
import pandas as pd


class HrCertification(models.Model):
    _name = 'hr.certification'
    _description = 'Certification des employés'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The name of the certification must be unique!')
    ]

    name = fields.Char('Name', required=True, index=True)
    description = fields.Text('Description')
    certification_employee_ids = fields.One2many('hr.certification.employee', 'certification_id', string='Employees with Certification')

    _sql_constraints = [
        ('unique_certification_employee', 'UNIQUE(certification_id, employee_id)', 'An employee cannot have the same certification more than once.')
    ]

    @api.constrains('certification_id', 'employee_id')
    def _check_unique_certification_employee(self):
        for record in self:
            if self.search_count([
                ('certification_id', '=', record.certification_id.id),
                ('employee_id', '=', record.employee_id.id),
                ('id', '!=', record.id)
            ]) > 0:
                raise ValidationError('An employee cannot have the same certification more than once.')