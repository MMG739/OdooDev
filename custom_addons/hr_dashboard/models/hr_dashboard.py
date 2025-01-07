from odoo import models, fields, api

class HRDashboard(models.Model):
    _name = 'hr.dashboard'
    _description = 'Tableau de Bord RH'

    total_employees = fields.Integer(string="Nombre Total d'Employés", compute='_compute_total_employees')
    employees_by_department = fields.Json(string="Répartition par Département", compute='_compute_employees_by_department')
    employees_by_experience = fields.Json(string="Répartition par Niveau d’Expérience", compute='_compute_employees_by_experience')
    low_performance_employees = fields.Many2many('hr.employee', string="Employés avec Faible Score", compute='_compute_low_performance_employees')

    @api.depends('total_employees')
    def _compute_total_employees(self):
        for record in self:
            record.total_employees = self.env['hr.employee'].search_count([])

    @api.depends('employees_by_department')
    def _compute_employees_by_department(self):
        for record in self:
            departments = self.env['hr.department'].search([])
            record.employees_by_department = [
                {'department': dep.name, 'count': self.env['hr.employee'].search_count([('department_id', '=', dep.id)])}
                for dep in departments
            ]

    @api.depends('employees_by_experience')
    def _compute_employees_by_experience(self):
        for record in self:
            levels = ['Débutant', 'Intermédiaire', 'Expert']
            record.employees_by_experience = [
                {'level': level, 'count': self.env['hr.employee'].search_count([('experience_level', '=', level)])}
                for level in levels
            ]

    @api.depends('low_performance_employees')
    def _compute_low_performance_employees(self):
        for record in self:
            record.low_performance_employees = self.env['hr.employee'].search([('performance_score', '<', 3.0)])
