import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('config.ini')

# path
GLOBAL_PATH = CONFIG.get('global', 'path')
SECRET_KEY = CONFIG.get('global', 'secret_key')
FLASK_DEBUG = CONFIG.getboolean('global', 'debug')
SERVER_NAME = CONFIG.get('global', 'server_name')

# database
MYSQL_DBNAME = CONFIG.get('mysql_db', 'name')
MYSQL_DBUSER = CONFIG.get('mysql_db', 'user')
MYSQL_DBPASS = CONFIG.get('mysql_db', 'pass')
MYSQL_DBHOST = CONFIG.get('mysql_db', 'host')

# mandrill
MANDRILL_KEY = CONFIG.get('mandrill', 'key')
SUPPORT_EMAIL = CONFIG.get('mandrill', 'from_email')
SUPPORT_NAME = CONFIG.get('mandrill', 'from_name')
SMTP_HOST = CONFIG.get('mandrill', 'smtp_host')
SMTP_USERNAME = CONFIG.get('mandrill', 'smtp_username')
SMTP_TO_ADDR = CONFIG.get('mandrill', 'smtp_to_user')

# mongo api
MONGO_API_HOST = CONFIG.get('mongo-api', 'host')
MONGO_API_VERSION = CONFIG.get('mongo-api', 'version')
MONGO_API_TOKEN = CONFIG.get('mongo-api', 'token')

# s3 storage
S3_API_KEY = CONFIG.get('s3-storage', 'api_key')
S3_SECRET_KEY = CONFIG.get('s3-storage', 'secret_key')
S3_BUCKET_NAME = CONFIG.get('s3-storage', 'bucket_name')
