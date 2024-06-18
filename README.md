# Récupération des Emails des Membres du Parlement Européen

Ce script Python utilise Selenium pour récupérer les adresses email des membres du Parlement Européen à partir d'une pays donné (ici la France). Il ouvre les profils des membres un par un, extrait les adresses email disponibles, et les affiche dans la console.

## Prérequis

- Python 3.x
- Navigateur Chrome installé

## Installation

1. Cloner le repository
   ```bash
   git clone https://github.com/lucasolerr/web-scrap-emails-from-europarl.git
   cd web-scrap-emails-from-europarl
   ```

2. Installer les dépendances du projet
    ```bash
    make install
    ```

3. Pour exécuter le script et récupérer les emails des membres du Parlement Européen :
    ```bash
    make run
    ```

### Commandes supplémentaires

- Formater le code avec ruff :
    ```bash
    make format
    ```
- Linter le code avec ruff :
    ```bash
    make format
    ```

## Structure du projet
- web_scrap_emails_from_europarl.py : Script principal pour récupérer les emails des membres.
- requirements.txt : Liste des dépendances Python requises.
- Makefile : Fichier pour automatiser les tâches comme l'installation, l'exécution, le formatage et le linter du code.
