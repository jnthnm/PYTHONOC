
# Le but est de crée un script de sauvegarde d'un fichier
# en particulier, et l'envoyer sur mon srv S3 AWS
 
# import datetime

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