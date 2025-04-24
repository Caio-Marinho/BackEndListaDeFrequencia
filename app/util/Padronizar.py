from app.service.ValidatesTypes import TipagemEstaticaFunction
from unidecode import unidecode

@TipagemEstaticaFunction
def padronizarNome(nome: str) -> str:
    return unidecode(nome.strip().title()) 

@TipagemEstaticaFunction
def padronizarEmail(email: str) -> str:
    return email.capitalize()