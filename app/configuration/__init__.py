# configuration/__init__.py
from dotenv import load_dotenv
from .configurationEnviroment import gerar_env_automatico
# Importar a classe Configuration
from .configuration import Configuration
# Carregar variáveis de ambiente do .env automaticamente
load_dotenv()

__all__ = ['Configuration', 'gerar_env_automatico', 'load_dotenv']