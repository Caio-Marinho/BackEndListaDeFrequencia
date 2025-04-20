from . import ValidatesTypes


@ValidatesTypes.TipagemEstaticaFunction
def validar_Nome(nome: str) -> bool:
    """Valida se o nome é válido"""
    # Implementação da validação do nome
    if len(nome) > 4:
        return True
    return False