# configuration/__init__.py
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env automaticamente
load_dotenv()

# Importar a classe Configuration
from .configuration import Configuration

__all__ = ['Configuration']