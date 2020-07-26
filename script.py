# Le but est de crée un script de sauvegarde et l'envoyer sur mon srv S3 AWS dans le bucket récuperer du fichier config JSON

# Liste des import
import os
import zipfile
import boto3
import datetime
import json
import logging
import timedelta 

from botocore.exceptions import ClientError

# Je charge mon fichier de config.json qui regroupe mon paramètre. 
with open('./config.json', 'r') as fichier:
    parametres = json.load(fichier)

# Je récupère la date d'aujourd'hui dans une variable datetoday
datetoday = datetime.date.today()
print("La date d'aujourd'hui est : " + " " + str(datetoday))

# Permet de verifié si le bucket est déja existant 
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
    create_bucket(parametres['bucketnom'],"us-west-2")

def create_bucket(bucket_name, region=None):
    # Création du bucket
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

# Je liste mes dossiers dans le chemin choisi
doclist = os.listdir(parametres["chemin"])
# J'affiche ma liste avec print
print("La liste des documents : " + " " + str(doclist))

# Je crée le nom du fichier avec la date du jour puis création du zip
nomdoc = 'Mesdocuments' + str(datetoday) + '.zip'
print(nomdoc)
creationzip = parametres["chemin"] + nomdoc 

# On utilise timedelta pour faire l'opération sur la date actuel
datesave = datetime.timedelta(parametres["joursdesave"])
print(datesave)
nom_todelete = 'Mesdocuments' + str(datetoday + datesave) + '.zip'
print(nom_todelete)

my_zip = zipfile.ZipFile(creationzip, 'w')

# On fait une boucle qui parcours les fichiers du dossier documents et qui crée notre zip
for file in doclist:
    if '.txt' in file:
       my_zip.write(os.path.join(parametres["chemin"], file))
            
my_zip.close()

# Push mon script sur mon serv S3 AWS 

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

# Delete du fichier défini dans le fichier de config.json
s3 = boto3.resource("s3")
obj = s3.Object(parametres['bucketnom'], nom_todelete)
obj.delete()
print("Le fichier zip nommé" + " " + nom_todelete + " " + "est supprimé du cloud S3 AWS du bucket nommé" + " " + parametres['bucketnom'])




