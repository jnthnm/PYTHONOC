# Automatic backup script to AWS on Windows

The purpose of this script is to perform an automatic backup of zip files to a cloud server hosted by AWS S3, also to delete files with a date defined in the JSON configuration file.

# Pre required for the script to work :

- Python 3.7.8
- Install pip install timedelta
- AWS CLI in order to automatically authenticate to our AWS S3 server (https://docs.aws.amazon.com/fr_fr/cli/latest/userguide/cli-chap-install.html)
- Github in order to get the script

# Operating mode :

We define our parameters in the configuration file named config.json

- "path": "The Path of the files to save",
- "bucketnom": "Bucket name which will be created on our S3 AWS server",
- "days of save": The number of days of save before the deletion of the file

Last step, you must use the Windows task scheduler so that the script can run automatically.
