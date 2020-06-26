
# Le but est de crée un script de sauvegarde de deux fichiers
#  et l'envoyer sur mon srv S3 AWS dans le bucket pythonscriptoc

# 1 - Lister tous les fichiers qui sont dans D:\Jonathan\Documents

# J'utilise import os afin de lister mes fichiers présents dans /J/Documents
import os
doclist = os.listdir("D:\Jonathan\Documents")
# J'affiche ma liste avec print
print(doclist)

# 2 - En faire un ZIP
import zipfile
# Je décide de crée mon fichier zip dans D:\Jonathan\Documents\ 'w : writemod'
my_zip = zipfile.ZipFile('D:\Jonathan\Documents\montest.zip', 'w')

# Je met les fichiers que je souhaite
my_zip.write('D:\Jonathan\Documents\doc.docx')
my_zip.write('D:\Jonathan\Documents\docdeux.docx')

my_zip.close()

# 3 - Utiliser CLI AWS pour s'authentifier (https://docs.aws.amazon.com/fr_fr/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration)

# AWS CONFIGURE
# On y rentre notre AWS Access Key ID & notre AWS Secret Access Key
print('Auth AWS OK')

# 4 - Push mon script sur mon serv S3 AWS (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html)

# Module boto3 
import boto3

s3 = boto3.resource('s3')
s3.meta.client.upload_file('D:\Jonathan\Documents\montest.zip', 'pythonscriptoc', 'montest.zip')
print ('Fichier ZIP UPLOADER dans le bucket pythonscriptoc')