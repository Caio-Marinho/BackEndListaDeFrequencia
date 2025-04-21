from .ValidatesNome import validar_Nome
from .ValidatesTypes import TipagemEstaticaClasse
import re
import json

@TipagemEstaticaClasse
class ValidatesData:
    """
    Classe para validar dados de entrada de um dicionário.

    Esta classe valida campos específicos de um dicionário, como email, nome e categoria,
    e armazena quaisquer erros de validação encontrados.
    """

    def __init__(self, data: dict):
        """
        Inicializa a classe com os dados a serem validados.

        :param data: Dicionário contendo os dados a serem validados.
        """
        self.__data = data
        self.__errors = []

    def validate(self) -> None:
        """
        Executa todas as validações nos dados fornecidos.

        Se houver erros de validação, eles são registrados e uma exceção ValueError é levantada.
        """
        self.validate_email()
        self.validate_nome()
        self.validate_categoria()
        
        if self.__errors:
            error_json = json.dumps({"errors": self.__errors})
            print(f"Validation errors: {error_json}")  # Log errors on the server
            raise ValueError(error_json)

    def validate_email(self) -> None:
        """
        Valida o campo de email no dicionário de dados.

        Adiciona um erro à lista de erros se o email estiver ausente ou não corresponder ao padrão esperado.
        """
        if not self.__data.get("email"):
            self.__add_error("email", "O email é Obrigatorio")
        elif not re.match(r'^(?![._%+@/\\-])[a-zA-Z0-9._%+-]+@ufpe\.br$', self.__data['email']):
            error_message = f"O email '{self.__data['email']}' é inválido."
            self.__add_error("email", error_message)

    def validate_nome(self) -> None:
        """
        Valida o campo de nome no dicionário de dados.

        Adiciona um erro à lista de erros se o nome estiver ausente, contiver caracteres inválidos,
        ou não atender aos critérios de comprimento mínimo.
        """
        if not self.__data.get("nome"):
            self.__add_error("nome", "O nome é Obrigatorio")
        elif not re.match(r'^[A-Za-z\s]+$', self.__data['nome']):
            error_message = f"O nome '{self.__data['nome']}' é inválido."
            self.__add_error("nome", error_message)
        elif not validar_Nome(self.__data['nome']):
            error_message = f"O Tamanho do nome '{self.__data['nome']}' é inválido pois devem possuir ao minimo 4 caracteres."
            self.__add_error("nome", error_message)

    def validate_categoria(self) -> None:
        """
        Valida o campo de categoria no dicionário de dados.

        Adiciona um erro à lista de erros se a categoria estiver ausente ou não for uma das categorias permitidas.
        """
        if not self.__data.get("categoria"):
            self.__add_error("categoria", "A categoria é Obrigatorio")
        else:
            tipo = ['calouro', 'calouros', 'Calouro', 'Calouros', 'voluntario', 'voluntarios', 'Voluntario', 'Voluntarios']
            if self.__data['categoria'] not in tipo:
                error_message = f"A categoria '{self.__data['categoria']}' é inválida."
                self.__add_error("categoria", error_message)

    def __add_error(self, field: str, message: str) -> None:
        """
        Adiciona um erro à lista de erros.

        :param field: O campo onde o erro ocorreu.
        :param message: A mensagem de erro a ser adicionada.
        """
        self.__errors.append({"field": field, "message": message})

    def get_errors(self) -> list:
        """
        Retorna a lista de erros de validação encontrados.

        :return: Lista de objetos contendo mensagens de erro.
        """
        return self.__errors