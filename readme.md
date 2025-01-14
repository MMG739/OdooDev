# OdooDev

## Description

Ce projet contient des modules personnalisés pour Odoo, incluant `exco_management` et `hr_custom`, qui ajoutent de nouvelles fonctionnalités pour la gestion des couleurs, des thèmes, des rapports Excel et des certifications des employés.

## Modules

### Exco Management

#### Fonctionnalités

- **Gestion des couleurs et thèmes** : Ajout de modèles pour gérer les couleurs (`AvailableColor`) et les thèmes (`CustomTheme`) de la page du menu, des boutons et de la navigation.
- **Génération de rapports Excel** : Création d'un modèle `excel.report.generator` pour générer des rapports Excel.

#### Détails Techniques

- **Initialisation et Manifest** :
  - Ajout de l'importation des `models` dans `__init__.py`.
  - Création de `__manifest__.py` pour définir les métadonnées et les dépendances du module.
  
- **Modèles et Vues** :
  - Nouveaux modèles `test_model`, `custom_settings`, et `report_excel_test` dans `models/__init__.py`.
  - Définition des modèles `AvailableColor` et `CustomTheme` dans `custom_settings.py`.
  - Création du modèle `excel.report.generator` dans `report_excel_test.py`.
  - Vues pour `available.color` et `custom.theme` dans `color_custom_views.xml`.

- **Sécurité et Assets** :
  - Mise à jour de `ir.model.access.csv` pour inclure les règles d'accès pour les nouveaux modèles.
  - Ajout de JavaScript pour l'application dynamique des thèmes dans `custom_theme.js` et inclusion dans `assets.xml`.

### HR Custom

#### Fonctionnalités

- **Gestion des certifications des employés** : Ajout du modèle `hr_certification_employee` pour lier les certifications et les employés, avec des contraintes garantissant des certifications uniques par employé.

#### Détails Techniques

- **Modèles et Contraintes** :
  - Ajout du modèle `hr_certification_employee` dans `models/__init__.py`.
  - Mise à jour de `hr_certification.py` pour inclure des contraintes et ajout de l'importation de pandas.
  - Modification de `hr_employee.py` pour utiliser la relation `One2many` pour les certifications.

- **Vues et Sécurité** :
  - Mise à jour de `hr_certification_views.xml` pour inclure les vues liste et kanban pour les certifications.
  - Mise à jour de `ir.model.access.csv` pour inclure les règles d'accès pour `hr_certification_employee`.

## Installation

1. Cloner le dépôt : `git clone https://github.com/MMG739/OdooDev.git`
2. Naviguer vers le répertoire du projet : `cd OdooDev`
3. Suivre les instructions d'installation pour Odoo et ajouter les modules personnalisés.

## Utilisation

- Configurer les paramètres de couleurs et thèmes via les vues `available.color` et `custom.theme`.
- Utiliser la fonction `generate_report_excel` pour générer des rapports Excel depuis le module correspondant.
- Gérer les certifications des employés via les vues et actions définies dans `hr_custom`.

## Contribuer

1. Forker le projet.
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/YourFeature`).
3. Commiter vos modifications (`git commit -am 'Add some feature'`).
4. Pousser votre branche (`git push origin feature/YourFeature`).
5. Ouvrir une pull request.

## Auteurs

- MMG739
