from flask import jsonify,send_file, request
from app.models import db, Discentes
from app.schema.schema import DiscenteSchema
from app.service.Discentes import AdiconarDiscentes
from . import routes


@routes.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        dados = request.get_json()
        discente = AdiconarDiscentes(dados)
        discente.validate()
        response = discente.salvar()
        return jsonify({'message': response}), 201
    
    if request.method == 'GET':
        discentes = Discentes.query.all()
        schema = DiscenteSchema(many=True)
        return jsonify(schema.dump(discentes)), 200