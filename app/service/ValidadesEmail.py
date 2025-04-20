from . import ValidatesTypes
import re

@ValidatesTypes.TipagemEstaticaFunction
def validar_email(email: str) -> bool:
    """Valida se o email é válido"""
    # Implementação da validação do email
    padrao = r'^(?![._%+-@/\])[a-zA-Z0-9._%+-]+@ufpe\.br$'
    if re.match(padrao, email):
        return True
    return False