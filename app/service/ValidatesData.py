from . import ValidatesTypes
import  re

@ValidatesTypes.TipagemEstaticaClasse
class ValidatesData:
    def __init__(self, data: dict):
        self.__data = data
        self.__errors = []

    def validate(self):
            self.validate_email()
            self.validate_nome()
            self.validate_categoria()

    def validate_email(self):
        if not re.match(r'^(?![._%+@/\\-])[a-zA-Z0-9._%+-]+@ufpe\.br$', self.__data['email']):
            error_message = f"O email '{self.__data['email']}' é inválido."
            self.__errors.append(error_message)
            raise ValueError(error_message)
            
    def validate_nome(self):
        if not re.match(r'^[A-Za-z\s]+$', self.__data['nome']):
            error_message = f"O nome '{self.__data['nome']}' é inválido."
            self.__errors.append(error_message)
            raise ValueError(error_message)
            
    def validate_categoria(self):
        tipo = ['calouro', 'calouros', 'Calouro', 'Calouros', 'voluntario', 'voluntarios', 'Voluntario', 'Voluntarios']
        if self.__data['categoria'] not in tipo:
            error_message = f"A categoria '{self.__data['categoria']}' é inválida."
            self.__errors.append(error_message)
            raise ValueError(error_message)