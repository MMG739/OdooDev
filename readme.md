# README

Pour l'exercice, j'ai d'abord créé le dossier `custom_addons`, puis j'ai créé le module `hr_custom` où j'ai réalisé l'extension du module `hr`.

# Exercice : Extension du module Employés (hr)

## Objectifs :
1. Comprendre la structure et les fonctionnalités du module `hr`.
2. Étendre et personnaliser ce module pour ajouter des fonctionnalités spécifiques.
3. Travailler avec les vues graphiques et rapports PDF.
4. S’entraîner à utiliser des données et graphiques dans Odoo.

## Partie 1 : Étude du module hr (Employés)
1. Familiarisation avec le module existant :
   - Identifiez les fonctionnalités clés du module `hr` :
     - Gestion des employés.
     - Informations personnelles et contrats.
   - Examinez les fichiers suivants :
     - `models/hr_employee.py` pour comprendre la structure des modèles.
     - `views/hr_employee_views.xml` pour voir comment les vues sont définies.
     - `data/hr.employee.csv` pour examiner les données exemple.
2. Questions pour réflexion :
   - Quels modèles sont utilisés par le module (par exemple, `hr.employee`) ?
   - Quels champs sont disponibles par défaut pour un employé ?
   - Quels menus et vues sont fournis par le module `hr` ?

## Partie 2 : Ajout de nouvelles fonctionnalités
1. Créer des champs personnalisés :
   - Ajoutez les champs suivants au modèle `hr.employee` :
     - Niveau d’expérience (`experience_level`, Selection avec des choix : 'Débutant', 'Intermédiaire', 'Expert').
     - Certifications (`certifications`, Many2many vers un nouveau modèle `hr.certification`).
     - Score de performance (`performance_score`, Float).
   - Ces champs doivent être visibles dans :
     - La vue formulaire des employés.
     - Une nouvelle vue liste dans le menu "Employés".
2. Créer un modèle pour les certifications :
   - Modèle: `hr.certification` avec les champs :
     - Nom de la certification (`name`, Char).
     - Description (`description`, Text).
     - Date d’obtention (`date_obtention`, Date).
   - Reliez ce modèle au modèle `hr.employee` via un champ Many2many.

## Partie 3 : Ajouter une vue graphique
1. Ajout d’une vue graphique pour les employés :
   - Ajoutez une vue graphique au menu "Employés" pour afficher :
     - La répartition des employés par niveau d’expérience (ex. : Débutant, Intermédiaire, Expert).
     - Le score de performance moyen par département.
2. Bonus :
   - Ajoutez des filtres dynamiques (ex. : filtrer par département, par responsable).

## Partie 4 : Rapport PDF
1. Créer un rapport PDF des employés :
   - Ajoutez un bouton "Exporter Rapport" dans la vue formulaire d’un employé.
   - Ce rapport doit inclure :
     - Les informations personnelles de l’employé (nom, département, manager).
     - Ses certifications.
     - Son score de performance.
   - Utilisez le moteur QWeb pour créer le template du rapport.
2. Mise en page :
   - Ajoutez un en-tête avec le logo de l’entreprise et une présentation professionnelle.
