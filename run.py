from app import criar_app
from app.configuration.configuration import Configuration


app = criar_app()
config = Configuration()

if __name__ == '__main__':
    
    from waitress import serve
    serve(app, host=config.FLASK_RUN_HOST, port=config.FLASK_RUN_PORT)