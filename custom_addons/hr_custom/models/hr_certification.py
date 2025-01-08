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