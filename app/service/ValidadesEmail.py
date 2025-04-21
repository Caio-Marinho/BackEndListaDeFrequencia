from .ValidatesTypes import TipagemEstaticaFunction
import re

@TipagemEstaticaFunction
def validar_email(email: str) -> bool:
    """
    Valida se o email é válido e pertence ao domínio 'ufpe.br'.

    Esta função verifica se o email fornecido está em um formato válido
    e se pertence ao domínio 'ufpe.br'. Utiliza expressões regulares para
    realizar a validação. Retorna True se o email for válido e pertence ao
    domínio especificado, caso contrário, retorna False.

    :param email: O endereço de email a ser validado.
    :return: Um booleano indicando se o email é válido (True) ou não (False).
    """
    # Expressão regular para validar o formato do email
    padrao: str = r'^(?![._%+-@/\])[a-zA-Z0-9._%+-]+@ufpe\.br$'
    if re.match(padrao, email):
        return True
    return False