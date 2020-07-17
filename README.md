# Script de sauvegarde automatique vers AWS 

Pre requis pour que le script fonctionne :

- Python 3.7.8
- CLI AWS
- Github

Fonctionnement :

On définit nos paramètres dans le fichier de configuration nommé config.json

- "chemin": "Le Chemin des fichiers à sauvegarder",
- "bucketnom": "Nom Du Bucket qui sera crée sur notre serveur S3 AWS",
- "joursdesave": Le nombre de jours de sauvegardes avant la suppréssion du fichier


