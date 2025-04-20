from . import ValidatesTypes

@ValidatesTypes.TipagemEstaticaFunction
def padronizarNome(texto: str) -> str:
    return texto.strip().title()

@ValidatesTypes.TipagemEstaticaFunction
def padronizarEmail(email: str) -> str:
    return email.capitalize()