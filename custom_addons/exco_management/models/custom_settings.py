from odoo import models, fields
import os

class AvailableColor(models.Model):
    _name = 'available.color'
    _description = 'Available Color'

    name = fields.Char(string="Nom de la couleur", required=True)
    color_code = fields.Char(string="Code couleur", required=True)  # Stocke les codes de couleur (ex: #FFFFFF)


class CustomTheme(models.Model):
    _name = 'custom.theme'
    _description = 'Custom Theme'

    color_main_navbar_id = fields.Many2one('available.color', string="Couleur de la barre de navigation")
    color_button_id = fields.Many2one('available.color', string="Couleur des boutons")

    def apply_theme_colors(self):
        # Récupérer les couleurs sélectionnées
        navbar_color = self.color_main_navbar_id.color_code
        button_color = self.color_button_id.color_code

        # Générer le contenu SCSS
        scss_content = f"""
        :root {{
            --color-main-navbar: var(--o-color-main-navbar, {navbar_color});
        }}

        .o_main_navbar {{
            background-color: var(--color-main-navbar);
        }}
        """

        # Chemin du fichier SCSS
        scss_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'src', 'scss')
        scss_path = os.path.join(scss_dir, 'custom_theme.scss')

        # Créer les répertoires s'ils n'existent pas
        os.makedirs(scss_dir, exist_ok=True)
        
        # Écrire le contenu SCSS dans le fichier
        with open(scss_path, 'w') as file:
            file.write(scss_content)

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }