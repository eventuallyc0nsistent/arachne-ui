import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('config.ini')

# path
GLOBAL_PATH = CONFIG.get('global', 'path')
SECRET_KEY = CONFIG.get('global', 'secret_key')
FLASK_DEBUG = CONFIG.getboolean('global', 'debug')
SERVER_NAME = CONFIG.get('global', 'server_name')

# database
DBNAME = CONFIG.get('sqllite', 'name')

# mandrill
MANDRILL_KEY = CONFIG.get('mandrill', 'key')
SUPPORT_EMAIL = CONFIG.get('mandrill', 'from_email')
SUPPORT_NAME = CONFIG.get('mandrill', 'from_name')
SMTP_HOST = CONFIG.get('mandrill', 'smtp_host')
SMTP_USERNAME = CONFIG.get('mandrill', 'smtp_username')
SMTP_TO_ADDR = CONFIG.get('mandrill', 'smtp_to_user')
