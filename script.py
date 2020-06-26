
# Le but est de crée un script de sauvegarde d'un fichier
# en particulier, et l'envoyer sur mon srv S3 AWS
 

# import datetime
# import zipfile

# J'utilise import os afin de lister mes fichiers présents dans /J/Documents
import os
doclist = os.listdir("D:\Jonathan\Documents")
# J'affiche ma liste avec print
print(doclist)
