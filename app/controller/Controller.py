import json
from app.globals import Response, jsonify,padronizarEmail,padronizarNome,datetime,HttpstatusCode
from app.schema.schema import DiscenteSchema
from app.service.Discentes import AdicionarDiscentes
from app.models.models import Discentes

http = HttpstatusCode()
class Controller:
    """
    Classe Controladora para gerenciar operações relacionadas aos 'Discentes'.
    Fornece métodos para cadastrar, listar e buscar usuários por ID, email e nome.
    """

    def __init__(self, discentes: dict = None):
        """
        Inicializa o Controlador com dados opcionais iniciais.

        :param discentes: Dicionário opcional contendo dados iniciais para um 'discente'.
        """
        self.__discente: dict = discentes or {}

    def get_dados(self) -> dict:
        """
        Recupera os dados atuais do 'discente'.

        :return: Um dicionário contendo os dados do 'discente'.
        """
        return self.__discente

    def set_dados(self, discente: dict) -> None:
        """
        Define os dados do 'discente'.

        :param discente: Um dicionário contendo os dados do 'discente' a serem definidos.
        """
        self.__discente = discente

    def CadastrarUsuario(self) -> Response:
        """
        Cadastra um novo 'discente' usando os dados fornecidos.

        :return: Um objeto Response do Flask contendo o resultado do processo de cadastro.
        """
        try:
            if self.RegistroNoDia(self.get_dados()['nome'], self.get_dados()['email']):
                return jsonify({'message': 'O discente ja foi cadastrado hoje'})
            # Cria uma instância de AdicionarDiscentes com os dados fornecidos
            discente: AdicionarDiscentes = AdicionarDiscentes(self.get_dados())
            # Salva o discente no banco de dados
            response: Response = discente.salvar()
            return response
        except Exception as e:
              # Retorna uma resposta de erro em caso de exceção
              response: Response = jsonify({'message': json.loads(str(e))})
              response.status_code = http.BadRequest.statusCode
              return response

    def ListarUsuarios(self) -> Response:
        """
        Lista todos os 'discentes' cadastrados.

        :return: Um objeto Response do Flask contendo uma lista de todos os 'discentes'.
        """
        try:
            # Consulta todos os discentes no banco de dados
            discentes: list = Discentes.query.all()
            # Serializa os dados usando o esquema DiscenteSchema
            schema: DiscenteSchema = DiscenteSchema(many=True)
            response: Response = jsonify(schema.dump(discentes))
            response.status_code = http.OK.statusCode
            return response
        except Exception as e:
            # Retorna uma resposta de erro em caso de exceção
            response: Response = jsonify({'message': json.loads(str(e))})
            response.status_code = http.BadRequest.statusCode
            return response
    
    def BuscarUsuarioID(self, id: int) -> Response:
        """
        Busca um 'discente' pelo ID.

        :param id: O ID do 'discente' a ser buscado.
        :return: Um objeto Response do Flask contendo o 'discente' encontrado.
        """
        try:
            # Busca o discente pelo ID
            discente: Discentes = Discentes.query.get(id)
            if discente:
                # Serializa os dados do discente encontrado
                schema: DiscenteSchema = DiscenteSchema()
                response: Response = jsonify(schema.dump(discente))
                response.status_code = 200
                return response
            else:
                # Retorna uma resposta de erro se o discente não for encontrado
                response: Response = jsonify({'message': 'discente nao foi encontrado'})
                response.status_code = 404
                return response
        except Exception as e:
            # Retorna uma resposta de erro em caso de exceção
            response: Response = jsonify({'message': json.loads(str(e))})
            response.status_code = 400
            return response
    
    def BuscarUsuarioEmail(self, email: str) -> Response:
        """
        Busca um 'discente' pelo email.

        :param email: O email do 'discente' a ser buscado.
        :return: Um objeto Response do Flask contendo o 'discente' encontrado.
        """
        try:
            # Padroniza o email e busca o discente pelo email
            discente: Discentes = Discentes.query.filter_by(email=padronizarEmail(email)).first()
            if discente:
                # Serializa os dados do discente encontrado
                schema: DiscenteSchema = DiscenteSchema()
                response: Response = jsonify(schema.dump(discente))
                response.status_code = 200
                return response
            else:
                # Retorna uma resposta de erro se o discente não for encontrado
                response: Response = jsonify({'message': 'discente nao foi encontrado'})
                response.status_code = 404
                return response
        except Exception as e:
            # Retorna uma resposta de erro em caso de exceção
            response: Response = jsonify({'message': json.loads(str(e))})
            response.status_code = 400
            return response
        
    def BuscarUsuarioNome(self, nome: str) -> Response:
        """
        Busca um 'discente' pelo nome.

        :param nome: O nome do 'discente' a ser buscado.
        :return: Um objeto Response do Flask contendo o 'discente' encontrado.
        """
        try:
            # Padroniza o nome e busca o discente pelo nome
            discente: Discentes = Discentes.query.filter_by(nome=padronizarNome(nome)).first()
            if discente:
                # Serializa os dados do discente encontrado
                schema: DiscenteSchema = DiscenteSchema()
                response: Response = jsonify(schema.dump(discente))
                response.status_code = 200
                return response
            else:
                # Retorna uma resposta de erro se o discente não for encontrado
                response: Response = jsonify({'erro': 'discente nao foi encontrado'})
                response.status_code = 404
                return response
        except Exception as e:
            # Retorna uma resposta de erro em caso de exceção
            response: Response = jsonify({'message': json.loads(str(e))})
            response.status_code = 400
            return response
    
    def BuscarQuantidadeRegistrosPorDiscente(self,nome:str, email:str) -> Response:
        """
        Busca a quantidade de registros de 'discente' no banco de dados.

        :return: Um objeto Response do Flask contendo a quantidade de registros de 'discente'.
        """
        try:
            # Busca a quantidade de registros de 'discente' com nome e email padronizados
            quantidade: int = Discentes.query.filter_by(
                nome=padronizarNome(self.get_dados()['nome']),
                email=padronizarEmail(self.get_dados()['email'])
            ).count()
            response: Response = jsonify({'quantidade_registros': quantidade})
            response.status_code = 200
            return response
        except Exception as e:
            # Retorna uma resposta de erro em caso de exceção
            response: Response = jsonify({'message': json.loads(str(e))})
            response.status_code = 400
            return response
        
    def RegistroNoDia(self,nome: str, email: str) -> Response:
        """
        Verifica se há registros de 'discente' no banco de dados para o dia atual.

        :return: Um objeto Response do Flask indicando se há registros no dia atual.
        """
        try:
            # Busca a quantidade de registros de 'discente' para o dia atual
            quantidade: int = Discentes.query.filter_by(
                nome=padronizarNome(nome),
                email=padronizarEmail(email),
                data=datetime.now().strftime('%Y-%m-%d')
            ).count()
            return True if quantidade else False
        except Exception as e:
            # Retorna uma resposta de erro em caso de exceção
            response: Response = jsonify({'message': json.loads(str(e))})
            response.status_code = 400
            return response