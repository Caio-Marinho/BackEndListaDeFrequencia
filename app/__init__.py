import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate,init,upgrade, migrate
from app.models import db
from app.schema import schema
from app.configuration import Configuration
from app.configuration.configurationEnviroment import gerar_env_automatico
from app.functions.log import configure_app_logging
from .routes.routes import routes
from dotenv import load_dotenv

def criar_app():
    
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    config = Configuration()
    
    # Se necessário, gere ou atualize o arquivo .env com base na configuração
    gerar_env_automatico(config.__dict__)
    
    # Cria a aplicação Flask
    app = Flask(__name__)
    
    # Configura o log
    configure_app_logging(app)
    
    
    # Carrega as configurações da classe Configuration no app.config
    app.config.from_object(config)
    
    # Inicializa extensões que dependem das configurações carregadas
    db.init_app(app)
    schema.init_app(app)
    Migrate(app, db)
    with app.app_context():
        if not os.path.exists('migrations'):  # Verificando se o diretório 'migrations' não existe.
            init()  # Inicializando as migrações.
        migrate()
        upgrade()
        
    
    # Registra rotas e configura o CORS
    app.register_blueprint(routes)
    CORS(app, resources={os.getenv('CORS_ORIGINS_WHITELIST','*'): {"origins": os.getenv('CORS_ALLOWED_ORIGINS','*')}})
    
    return app