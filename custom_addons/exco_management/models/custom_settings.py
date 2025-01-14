import base64
import io
import xlsxwriter
from odoo import models, fields, api
from odoo.exceptions import UserError

class AvailableColor(models.Model):
    _name = 'available.color'
    _description = 'Available Color'

    name = fields.Char(string="Nom de la couleur", required=True)
    color_code = fields.Char(string="Code couleur", required=True)  # Stocke les codes de couleur (ex: #FFFFFF)

    def generate_excel_report(self):
        selected_ids = self.env.context.get('active_ids', [])
        selected_records = self.env['available.color'].browse(selected_ids)
        
        fields_to_export = [
            {'name': 'name', 'string': 'Nom de la couleur'},
            {'name': 'color_code', 'string': 'Code couleur'},
        ]

        return self.env['excel.report.generator'].generate_excel_report(
            records=selected_records,
            fields_to_export=fields_to_export,
            filename='AvailableColors.xlsx'
        )

class CustomTheme(models.Model):
    _name = 'custom.theme'
    _description = 'Custom Theme'

    color_main_navbar_id = fields.Many2one('available.color', string="Couleur de la barre de navigation")
    color_web_id = fields.Many2one('available.color', string="Couleur de la page")
    color_button_id = fields.Many2one('available.color', string="Couleur des boutons")
    color_menu_id = fields.Many2one('available.color', string="Couleur du menu")

    def apply_theme_colors(self):
        # Récupérer les couleurs sélectionnées
        navbar_color = self.color_main_navbar_id.color_code
        web_color = self.color_web_id.color_code
        button_color = self.color_button_id.color_code
        menu_color = self.color_menu_id.color_code

        # Générer le contenu CSS
        css_content = f"""
        .o_main_navbar {{
            background-color: {navbar_color};
        }}
        .o_web_client {{
            background-color: {web_color};
        }}
        .btn-primary {{
            --btn-bg:{button_color};
        }}

        .o_main_navbar .o_menu_sections .o_nav_entry {{
            background: {menu_color};
        }}
        """

        # Retourner le CSS pour injection dynamique via JavaScript
        return {
            'type': 'ir.actions.client',
            'tag': 'custom_theme_apply',
            'params': {'css': css_content},
        }
