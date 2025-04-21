import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

def configure_app_logging(app):
    # Carrega as variáveis de ambiente
    load_dotenv()

    # Parâmetros de configuração para o log
    LOG_PATH = os.getenv('LOG_PATH', 'log')
    LOG_FILE_NAME = os.getenv('LOG_FILE_NAME', 'app.log')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
    LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s - %(levelname)s - %(message)s')
    LOG_DATE_FORMAT = os.getenv('LOG_DATE_FORMAT', '%Y-%m-%d %H:%M:%S')
    LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES', 5 * 1024 * 1024))  # 5 MB
    LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', 3))
    LOG_ENCODING = os.getenv('LOG_ENCODING', 'utf-8')
    LOG_MODE = os.getenv('LOG_MODE', 'a')

    # Cria o diretório de log, se necessário
    os.makedirs(LOG_PATH, exist_ok=True)
    log_file_path = os.path.join(LOG_PATH, LOG_FILE_NAME)

    # Cria o formatter e os handlers (RotatingFileHandler para arquivo e StreamHandler para console)
    formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding=LOG_ENCODING,
        mode=LOG_MODE
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(LOG_LEVEL)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(LOG_LEVEL)

    # Configura o logger da aplicação:
    # Limpa os handlers antigos para evitar duplicação (se já estiver configurado)
    app.logger.handlers.clear()
    app.logger.setLevel(LOG_LEVEL)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    # Configura o logger do werkzeug (servidor do Flask)
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.handlers.clear()
    werkzeug_logger.setLevel(LOG_LEVEL)
    werkzeug_logger.addHandler(file_handler)
    werkzeug_logger.addHandler(stream_handler)

    # Log opcional para confirmar a configuração
    app.logger.info("Logging configurado com sucesso!")