# Script de sauvegarde automatique vers AWS sur Windows 

Ce script a pour objectif d'effectuer une sauvegarde automatique de fichiers zip vers un serveur cloud hébérgé par AWS S3, de supprimé également des fichiers avec une date défini dans le fichier de configuration JSON.

# Pre requis pour que le script fonctionne :

- Python 3.7.8
- Installer pip install timedelta
- CLI AWS afin de s'authentifié à notre serveur AWS S3 de façon automatique (https://docs.aws.amazon.com/fr_fr/cli/latest/userguide/cli-chap-install.html)
- Github afin de récuperer le script 

# Mode de fonctionnement :

On définit nos paramètres dans le fichier de configuration nommé config.json

- "chemin": "Le Chemin des fichiers à sauvegarder",
- "bucketnom": "Nom Du Bucket qui sera crée sur notre serveur S3 AWS",
- "joursdesave": Le nombre de jours de sauvegardes avant la suppréssion du fichier

Dernière étape, il faut utiliser le planificateur de tâches Windows pour que le script puisse s'éxecuter automatiquement.









