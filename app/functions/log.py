
import os
import logging
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar logging
log_level = os.getenv('LOG_LEVEL', 'INFO')
log_file_name = os.getenv('LOG_FILE_PATH', 'app.log')
log_directory = os.getenv('LOG_PATH', 'app/log')
log_file_mode = os.getenv('LOG_FILE_MODE', 'a')
log_format = os.getenv('LOG_FORMAT', '%(asctime)s - %(levelname)s - %(message)s')
log_date_format = os.getenv('LOG_DATE_FORMAT', '%Y-%m-%d %H:%M:%S %z')
log_encoding = os.getenv('LOG_ENCODING', 'UTF-8')

# Criar diretório de log se não existir
os.makedirs(log_directory, exist_ok=True)

# Caminho completo do arquivo de log
log_file_path = os.path.join(log_directory, log_file_name)

logging.basicConfig(
    level=log_level,
    format=log_format,
    datefmt=log_date_format,
    handlers=[
        logging.FileHandler(log_file_path, mode=log_file_mode, encoding=log_encoding),
        logging.StreamHandler()
    ]
)