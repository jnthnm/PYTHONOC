# Le but est de crée un script de sauvegarde de deux fichiers
#  et l'envoyer sur mon srv S3 AWS dans le bucket pythonscriptoc
# - Lister tous les fichiers qui sont dans D:\Jonathan\Documents
# - Integrer la date dans le nom du fichier de sauvegarde zip et delete le fichier zip à la fin ainsi que trouver un moyen
# pour que AWS me confirme que le zip est bien uploadé

# J'utilise import os afin de lister mes fichiers présents dans /J/Documents

import os
import zipfile
import boto3
import datetime
import json
import logging

# Je récupère la date d'aujourd'hui dans une variable datetoday

datetoday = datetime.date.today()
print("La date d'aujourd'hui est : " + " " + str(datetoday))

# Je charge mon fichier de config.json qui regroupe mon paramètre. 
with open('./config.json', 'r') as fichier:
    parametres = json.load(fichier)

# Je liste mes dossiers dans le chemin choisi
doclist = os.listdir(parametres["chemin"])
# J'affiche ma liste avec print
print("La liste des documents : " + " " + str(doclist))

# Je crée le nom du fichier avec la date du jour puis création du zip
nomdoc = 'Mesdocuments' + str(datetoday) + '.zip'
creationzip = parametres["chemin"] + nomdoc 
print(nomdoc)

my_zip = zipfile.ZipFile(creationzip, 'w')

# On fait une boucle qui parcours les fichiers du dossier documents et qui crée notre zip
for file in doclist:
    if '.txt' in file:
       my_zip.write(os.path.join(parametres["chemin"], file))
            
my_zip.close()

# S'authentifié avec le CLI D'AWS
# Push mon script sur mon serv S3 AWS (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html)

import boto3

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(creationzip, bucket, nomdoc)
        print("Upload OK")
        return True
    except FileNotFoundError:
        print("Fichier pas trouvé")
        return False

uploaded = upload_to_aws('creationzip', 'pythonscriptoc', nomdoc)

# Proceder au delete du fichier zip
try:
    os.remove(creationzip)
except OSError as e:
    print(e)
else:
    print("Le fichier zip nommé" + " " + nomdoc + " " + "est supprimé")

