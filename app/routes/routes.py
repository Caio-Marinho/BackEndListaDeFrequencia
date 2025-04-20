from flask import jsonify,send_file, request
from app.models.models import db,Discentes
from . import routes

@routes.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        dados = request.get_json()
        discentes = Discentes(dados['nome'],dados['email'],dados['horas'],dados['dias'],dados['categoria'])
        db.session.add(discentes)
        db.session.commit()
    
    return jsonify({'message': dados}), 200