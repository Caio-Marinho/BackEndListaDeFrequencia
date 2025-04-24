from .globals import  Migrate, init, upgrade, migrate, routes, Configuration, gerar_env_automatico, CORS, load_dotenv, Flask, os
from .functions import configure_app_logging
from app.models import db
from app.schema import ma


class AppFactory:
    def __init__(self):
        load_dotenv()
        self.config = Configuration()
        gerar_env_automatico(self.config.__dict__)
        self.app = Flask(__name__)
        self.configure_app()

    def configure_app(self):
        self.app.config.from_object(self.config)
        configure_app_logging(self.app)
        db.init_app(self.app)
        ma.init_app(self.app)
        Migrate(self.app, db)
        
        with self.app.app_context():
            from .util.HttpStatus import HttpstatusCode
            if not os.path.exists('migrations'):
                init()
            migrate()
            upgrade()

        self.app.register_blueprint(routes)
        CORS(self.app, resources={
            os.getenv('CORS_ORIGINS_WHITELIST', '*'): {
                "origins": os.getenv('CORS_ALLOWED_ORIGINS', '*')
            }
        })

   
    def app(self):
        return self.app
    
    
    

criar_app = AppFactory()