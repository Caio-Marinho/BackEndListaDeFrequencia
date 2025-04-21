from app.controller.Controller import Controller
from flask import request, jsonify

def index_view():
    """
    Função de visualização para a rota raiz da aplicação.

    Esta função é responsável por lidar com as requisições GET e POST para a rota raiz.
    Ela instancia a classe Controller e delega a ela a responsabilidade de lidar com as operações.

    Returns:
        Response: Objeto Response do Flask indicando o resultado da operação.
    """
    controller: Controller = Controller()
    if request.method == 'POST':
        """
        Se a requisição for do tipo POST, a função irá cadastrar um novo discente.
        """
        controller.set_dados(request.get_json())
        return controller.CadastrarUsuario()
    elif request.method == 'GET':
        """
        Se a requisição for do tipo GET, a função irá listar todos os discentes cadastrados.
        """
        return controller.ListarUsuarios()
    else:
        """
        Se a requisição for de um tipo diferente de GET ou POST, a função irá retornar uma resposta de erro.
        """
        return jsonify({'message': 'Method not allowed'}), 405