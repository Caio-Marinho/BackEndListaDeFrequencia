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
        self.__errors = {}

    def validate(self) -> None:
        """
        Executa todas as validações nos dados fornecidos.

        Se houver erros de validação, eles são registrados e uma exceção ValueError é levantada.
        """
        self.validate_email()
        self.validate_nome()
        self.validate_categoria()
        
        if self.__errors:
            raise ValueError(self.get_errors())

    def validate_email(self) -> None:
        """
        Valida o campo de email no dicionário de dados.
        """
        if not self.__data.get("email"):
            self.__add_error("email", "O email é Obrigatório")
        elif not re.match(r'^(?![._%+@/\\-])[a-zA-Z0-9._%+-]+@ufpe\.br$', self.__data['email']):
            error_message = f"O email '{self.__data['email']}' é inválido."
            self.__add_error("email", error_message)

    def validate_nome(self) -> None:
        """
        Valida o campo de nome no dicionário de dados.
        """
        if not self.__data.get("nome"):
            self.__add_error("nome", "O nome é Obrigatório")
        elif not re.match(r'^[A-Za-z\s]+$', self.__data['nome']):
            error_message = f"O nome '{self.__data['nome']}' é inválido."
            self.__add_error("nome", error_message)
        elif not validar_Nome(self.__data['nome']):
            error_message = f"O Tamanho do nome '{self.__data['nome']}' é inválido, deve ter no mínimo 4 caracteres."
            self.__add_error("nome", error_message)

    def validate_categoria(self) -> None:
        """
        Valida o campo de categoria no dicionário de dados.
        """
        if not self.__data.get("categoria"):
            self.__add_error("categoria", "A categoria é Obrigatória")
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
        if field not in self.__errors:
            self.__errors[field] = ""
        self.__errors[field] = message

    def get_errors(self) -> str:
        """
        Retorna a lista de erros de validação encontrados no formato JSON.

        :return: JSON string com mensagens de erro por campo.
        """
        return json.dumps({"errors": self.__errors}, ensure_ascii=False, indent=2)
