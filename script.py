
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

datetoday = datetime.date.today()
print("La date d'aujourd'hui est : " + " " + str(datetoday))

# Je charge mon fichier de config.json qui regroupe mes paramètres. 
with open('./config.json', 'r') as fichier:
    parametres = json.load(fichier)

doclist = os.listdir(parametres["chemin"])
# J'affiche ma liste avec print
print("La liste des documents : " + " " + str(doclist))

nomdoc = 'Mesdocuments' + str(datetoday) + '.zip'
creationzip = parametres["chemin"] + nomdoc 
 #print("Le chemin est" + " " + str(nomdoc) + " " + "et la date est le" + " " + str(datetoday))
#nomdoc = parametres["chemin"] + 'Mesdocuments' + str(datetoday) + '.zip'
print(nomdoc)

#nomdoc = 'Mesdocuments' + str(datetoday) + '.zip'
 #print("Le chemin est" + " " + str(nomdoc) + " " + "et la date est le" + " " + str(datetoday))
#creationzip = parametres["chemin"] + nomdoc + '.zip'
#+ str(datetoday) + '.zip'
#print(nomdoc)


# Je décide de crée mon fichier zip dans D:\Jonathan\Documents\ 'w : writemod'
my_zip = zipfile.ZipFile(creationzip, 'w')

# On fait une boucle qui parcours les fichiers du dossier documents
# Et qui crée notre zip
for file in doclist:
    if '.txt' in file:
       my_zip.write(os.path.join(parametres["chemin"], file))
            
my_zip.close()

# 4 - Push mon script sur mon serv S3 AWS (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html)

from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
s3.meta.client.upload_file(creationzip, 'pythonscriptoc', nomdoc)

#s3.meta.client.upload_file(creationzip, 'pythonscriptoc', nomdoc)
   

# Proceder au delete du fichier zip
try:
        os.remove(creationzip)
except OSError as e:
        print(e)
else:
        print("File is deleted successfully")
