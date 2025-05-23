import os
import sqlalchemy
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Configuration:
    load_dotenv()
    def __init__(self): 
        # Use environment variables for database credentials
        self.DB_USER = os.getenv('DB_USER', 'root')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'teste')
        self.DB_HOST = os.getenv('DB_HOST', 'localhost')
        self.DB_PORT = os.getenv('DB_PORT', '3306')
        self.DB_NAME = os.getenv('DB_NAME', 'frequencia')

        # Create engine and ensure database exists
        self.engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/')
        logging.debug("Conectando no servidor de banco de dados para garantir que o banco de dados exista.")
        with self.engine.connect() as connection:
            connection.execute(sqlalchemy.text(f"CREATE DATABASE IF NOT EXISTS {self.DB_NAME};"))
            logging.debug(f"Banco de dados {self.DB_NAME} descrito existe.")

        # Configuration settings
        self.SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', f'mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')
        logging.debug(f"SQLALCHEMY_DATABASE_URI está inserido: {self.SQLALCHEMY_DATABASE_URI}")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = 'True'.lower() in ['true', '1', 'yes']
        self.SQLALCHEMY_ECHO = 'True'.lower() in ['true', '1', 'yes']
        self.SQLALCHEMY_ENCODING = 'UTF-8'
        self.SQLALCHEMY_POOL_RECYCLE = int('300')
        self.SQLALCHEMY_POOL_SIZE = int('5')
        self.SQLALCHEMY_MAX_OVERFLOW = int('10')
        self.SQLALCHEMY_POOL_TIMEOUT = int('30')
        self.SQLALCHEMY_COMMIT_ON_TEARDOWN = 'True'.lower() in ['true', '1', 'yes']
        self.SQLALCHEMY_RECORD_QUERIES = 'True'.lower() in ['true', '1', 'yes']
        self.SQLALCHEMY_SILENCE_UBER_WARNING = 'True'.lower() in ['true', '1', 'yes']
        self.FLASK_APP = 'run.py'
        self.FLASK_ENV = 'development'
        self.FLASK_DEBUG = 'True'.lower() in ['true', '1', 'yes']
        self.FLASK_RUN_HOST = '0.0.0.0'
        self.FLASK_RUN_PORT = int('5000')
        self.FLASK_SECRET_KEY = os.urandom(24).hex()
        self.FLASK_STATIC_FOLDER = 'static'
        self.FLASK_TEMPLATE_FOLDER = 'templates'
        self.FLASK_DEBUG_TB_ENABLED = 'True'.lower() in ['true', '1', 'yes']
        self.FLASK_DEBUG_TB_INTERCEPT_REDIRECTS = 'True'.lower() in ['true', '1', 'yes']
        self.FLASK_DEBUG_TB_TEMPLATE_FOLDER = 'debug_toolbar/templates'
        
        # CORS configuration
        self.CORS_ALLOWED_ORIGINS = '*'
        self.CORS_SUPPORTS_CREDENTIALS = 'True'.lower() in ['true', '1', 'yes']
        self.CORS_ORIGINS_WHITELIST = '*'
        self.CORS_MAX_AGE = int('3600')
        self.CORS_RESOURCES = '*'

        # Email configuration
        self.MAIL_SERVER = 'smtp.example.com'
        self.MAIL_PORT = int('587')
        self.MAIL_USERNAME = 'user@example.com'
        self.MAIL_PASSWORD = 'password'
        self.MAIL_USE_TLS = 'True'.lower() in ['true', '1', 'yes']
        self.MAIL_USE_SSL = 'False'.lower() in ['true', '1', 'yes']

        # Timezone configuration
        self.TIMEZONE = 'America/Recife'

        # Log configuration
        self.LOG_LEVEL = 'INFO'.upper()
        self.LOG_FILE_PATH = 'app.log'
        self.LOG_FILE_NAME = 'app.log'
        self.LOG_PATH = 'app/log'
        self.LOG_FILE_MODE = 'a+'
        self.LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
        self.LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S %z'
        self.LOG_ENCODING = 'UTF-8'  # Added UTF-8 encoding for logs

        # Application information
        self.APP_NAME = 'ListaDeFequencia'
        self.APP_VERSION =  '2.0.0'

        # Monitoring directory
        self.MONITORING_DIRECTORY = 'app/logs'
        self.MONITORING_FILE = 'application.log'

        # Swagger configuration
        self.SWAGGER_TITLE = 'API Documentation'
        self.SWAGGER_DESCRIPTION = 'API para gerenciamento de frequencia de alunos.'
        self.SWAGGER_VERSION = '1.0.0'
        
        # JWT configuration
        self.JWT_SECRET_KEY = os.urandom(24).hex()
        self.JWT_ACCESS_TOKEN_EXPIRES = 3600
        self.JWT_REFRESH_TOKEN_EXPIRES = 86400

        # Redis configuration
        self.REDIS_HOST = 'localhost'
        self.REDIS_PORT = 6379  
        self.REDIS_DB = 0

        # Celery configuration
        self.CELERY_BROKER_URL = 'redis://localhost:6379/0'
        self.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
        self.CELERY_ACCEPT_CONTENT = ['application/json']
        self.CELERY_TASK_SERIALIZER = 'json'
        self.CELERY_RESULT_SERIALIZER = 'json'
        self.CELERY_TIMEZONE = 'America/Recife'
        self.CELERY_ENABLE_UTC = True

        # Sentry configuration
        self.SENTRY_DSN = 'https://example.sentry.io/12345'
        self.SENTRY_ENVIRONMENT = 'development'
        