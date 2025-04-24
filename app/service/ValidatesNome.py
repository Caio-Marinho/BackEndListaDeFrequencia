from .ValidatesTypes import TipagemEstaticaFunction
import re


@TipagemEstaticaFunction
def validar_Nome(nome: str) -> bool:
    """Valida se o nome é válido"""
    # Implementação da validação do nome
    if len(nome) >= 3:
        return True
    return False

@TipagemEstaticaFunction
def ValidarFomato(nome: str) -> bool:
    padrao:str = r'^([A-Z][a-z]+)(\s[A-Z][a-z]+)*$'
    if re.fullmatch(padrao, nome):
        return True
    return False