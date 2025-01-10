from odoo import models, fields, http

class AvailableColor(models.Model):
    _name = 'available.color'
    _description = 'Available Color'

    name = fields.Char(string="Nom de la couleur", required=True)
    color_code = fields.Char(string="Code couleur", required=True)  # Stocke les codes de couleur (ex: #FFFFFF)


class CustomTheme(models.Model):
    _name = 'custom.theme'
    _description = 'Custom Theme'

    color_main_navbar_id = fields.Many2one('available.color', string="Couleur de la barre de navigation")
    color_web_id = fields.Many2one('available.color', string="Couleur de la page")

    def apply_theme_colors(self):
        # Récupérer les couleurs sélectionnées
        navbar_color = self.color_main_navbar_id.color_code
        web_color = self.color_web_id.color_code

        # Générer le contenu CSS
        css_content = f"""
        .o_main_navbar {{
            background-color: {navbar_color};
        }}
        .o_web_client {{
            background-color: {web_color};
        }}
        """

        # Retourner le CSS pour injection dynamique via JavaScript
        return {
            'type': 'ir.actions.client',
            'tag': 'custom_theme_apply',
            'params': {'css': css_content},
        }
