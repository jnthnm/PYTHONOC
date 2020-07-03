
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

datetoday = datetime.date.today()

# Je charge mon fichier de config.json qui regroupe mes paramètres. 
with open('./config.json', 'r') as fichier:
    parametres = json.load(fichier)
print(parametres["chemincfg"])

doclist = os.listdir(parametres["chemincfg"])
# J'affiche ma liste avec print
print("La liste des documents : " + " " + str(doclist))

monchemin = 'D:\Jonathan\Documents\documents' + str(datetoday) + '.zip'
print("Le chemin est" + " " + str(monchemin) + " " + "et la date est le" + " " + str(datetoday))

# Je décide de crée mon fichier zip dans D:\Jonathan\Documents\ 'w : writemod'
my_zip = zipfile.ZipFile(monchemin, 'w')

# On fait une boucle qui parcours les fichiers du dossier documents
# Et qui crée notre zip
for file in doclist:
    if '.txt' in file:
       my_zip.write(os.path.join("D:\Jonathan\Documents", file))
            
my_zip.close()
print("Fichier ZIP Crée")
    
# 2 - En faire un ZIP
# 3 - Utiliser CLI AWS pour s'authentifier (https://docs.aws.amazon.com/fr_fr/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration)

# AWS CONFIGURE -> On y rentre notre AWS Access Key ID & notre AWS Secret Access Key
#print('Auth AWS OK')

# 4 - Push mon script sur mon serv S3 AWS (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html)
# Module boto3 

#s3 = boto3.resource('s3')
#s3.meta.client.upload_file('D:\Jonathan\Documents\montest.zip', 'pythonscriptoc', 'montest.zip')

