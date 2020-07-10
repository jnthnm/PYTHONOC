# Le but est de crée un script de sauvegarde et l'envoyer sur mon srv S3 AWS dans le bucket pythonscriptoc
# Utilisation du planificateur de tâches de windows afin d'executer le script automatique tous les jours

# Liste des import

import os
import zipfile
import boto3
import datetime
import json
import logging
from botocore.exceptions import ClientError

# Je récupère la date d'aujourd'hui dans une variable datetoday

datetoday = datetime.date.today()
print("La date d'aujourd'hui est : " + " " + str(datetoday))

# Je charge mon fichier de config.json qui regroupe mon paramètre. 
with open('./config.json', 'r') as fichier:
    parametres = json.load(fichier)

print(parametres['bucketnom'])

def create_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': 'us-west-2'}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
create_bucket(parametres['bucketnom'],"us-west-2")

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

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(creationzip, bucket, nomdoc)
        print("Upload OK")
        return True
    except FileNotFoundError:
        print("Fichier pas trouvé")
        return False

uploaded = upload_to_aws('creationzip', parametres['bucketnom'], nomdoc)

# Proceder au delete du fichier zip
try:
    os.remove(creationzip)
except OSError as e:
    print(e)
else:
    print("Le fichier zip nommé" + " " + nomdoc + " " + "est supprimé")

bucketexist = False
s3 = boto3.client('s3')
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
    if bucket["Name"] == parametres['bucketnom']:
        bucketexist = True

if bucketexist: 
    print('Le bucket existe') 
else:
    print('Le bucket n\'existe pas') 
    # Rajouter création du bucket nommé dans le json      

# Supprimé des fichiers qui date de 3 jours 
# Rajouter un cloud azure
# Utiliser planificateur de tâches windows pour exec le script automatiquement