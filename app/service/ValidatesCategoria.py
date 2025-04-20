from . import ValidatesTypes

@ValidatesTypes.TipagemEstaticaClasse
class ValidarCategoria:
    def __init__(self, categoria: str):
        self.__categoria = categoria
        self.__validade = self.get_validade()
    
    def get_validade(self):
        return self.__validade
    
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria: str):
        self.__categoria = categoria
        tipo = ['calouro','calouros','Calouro','Calouros','voluntario','voluntarios','Voluntario','Voluntarios']
        if categoria not in tipo:
            self.__validade = False
        else:
            self.__validade = True

    