import logging
from logging.handlers import RotatingFileHandler
from venv import logger
import time
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

LOG_PATH = os.getenv('LOG_PATH', 'log')
LOG_FILE_NAME = os.getenv('LOG_FILE_NAME', 'app.log')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s - %(levelname)s - %(message)s')
LOG_DATE_FORMAT = os.getenv('LOG_DATE_FORMAT', '%Y-%m-%d %H:%M:%S')
LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES', 5 * 1024 * 1024))
LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', 3))
LOG_ENCODING = os.getenv('LOG_ENCODING', 'utf-8')
LOG_MODE = os.getenv('LOG_MODE', 'a')

# Criar o diretório de log
os.makedirs(LOG_PATH, exist_ok=True)
log_file_path = os.path.join(LOG_PATH, LOG_FILE_NAME)

# Configuração de logging
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=LOG_DATE_FORMAT,
    handlers=[
        RotatingFileHandler(log_file_path, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Configurar logging do werkzeug (servidor Flask)
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(LOG_LEVEL)
werkzeug_logger.addHandler(logging.FileHandler(log_file_path, mode=LOG_MODE, encoding=LOG_ENCODING))
werkzeug_logger.addHandler(logging.StreamHandler())

def monitor_eventos():
    logger.info("Monitoramento paralelo iniciado.")
    logger.debug("Evento do sistema registrado a cada alteração.")
    logger.info("Monitoramento paralelo iniciado.")