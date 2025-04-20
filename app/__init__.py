import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate,init
from app.models import db
from app.schema import schema
from app.configuration import Configuration
from app.configuration.configurationEnviroment import gerar_env_automatico
import app.functions.log
from .routes.routes import routes
from dotenv import load_dotenv

def criar_app():
    
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Se necessário, gere ou atualize o arquivo .env com base na configuração
    gerar_env_automatico(Configuration().__dict__)
    
    # Cria a aplicação Flask
    app = Flask(__name__)
    
    # Carrega as configurações da classe Configuration no app.config
    app.config.from_object(Configuration())
    
    # Inicializa extensões que dependem das configurações carregadas
    db.init_app(app)
    schema.init_app(app)
    Migrate().init_app(app, db)
    
    with app.app_context():
        if not os.path.exists('migrations'):  # Verificando se o diretório 'migrations' não existe.
            init()  # Inicializando as migrações.
        db.create_all()
    
    # Registra rotas e configura o CORS
    app.register_blueprint(routes)
    CORS(app)
    
    return app