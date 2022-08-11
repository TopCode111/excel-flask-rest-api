# Statement for enabling the development environment
DEBUG = False

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/downpos'
#SQLALCHEMY_TRACK_MODIFICATIONS = False
#
# # Application threads. A common general assumption is
# # using 2 per available processor cores - to handle
# # incoming requests using one and performing background
# # operations using the other.
# THREADS_PER_PAGE = 2
#
# # Enable protection agains *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED = True
#
# # Use a secure, unique and absolutely secret key for
# # signing the data.
# CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

AWS_ACCESS_KEY_ID = 'AKIA3X4HPQTFERPDUJUF'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'miraie-image-storage-tmp'
AWS_S3_REGION_NAME = "ap-northeast-1"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
