/** @odoo-module **/

import { registry } from "@web/core/registry";

// Enregistrer l'action `custom_theme_apply` dans la catégorie `actions`
registry.category("actions").add("custom_theme_apply", async (env, action) => {
    
    console.log("Action custom_theme_apply appelée", {
        timestamp: new Date().toISOString(),
        params: action.params.css
    });
    const cssContent = action.params.css;
    if (cssContent) {
        localStorage.setItem('customCss', cssContent);
        injectStyles(cssContent);
    }
});
// Fonction pour injecter dynamiquement le CSS dans le document
function injectStyles(cssContent) {
    let styleTag = document.getElementById('custom-dynamic-styles');
    if (!styleTag) {
        styleTag = document.createElement('style');
        styleTag.id = 'custom-dynamic-styles';
        document.head.appendChild(styleTag);
    }
    styleTag.innerHTML = cssContent;
}

// Charger les styles personnalisés depuis le localStorage au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    const savedCss = localStorage.getItem('customCss');
    if (savedCss) {
        injectStyles(savedCss);
    }
});
