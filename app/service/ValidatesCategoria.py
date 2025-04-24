from .ValidatesTypes import TipagemEstaticaClasse

@TipagemEstaticaClasse
class ValidarCategoria:
    def __init__(self, categoria: str):
        self.__categoria = categoria
        self.__validade = None  # Inicializa validade com None
        self.valido = categoria  # Chama o setter para validar a categoria
    
    @property
    def valido(self):
        return self.__validade
    
    @valido.setter
    def valido(self, categoria: str):
        tipo = ['calouro', 'calouros', 'Calouro', 'Calouros', 'voluntario', 'voluntarios', 'Voluntario', 'Voluntarios']
        if categoria in tipo:
            self.__validade = True  # Categoria inválida
        else:
            self.__validade = False  # Categoria válida
    
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria: str):
        self.valido = categoria  # Chama o setter para validar a categoria