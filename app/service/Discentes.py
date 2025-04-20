from app.service.ValidatesData import ValidatesData
from app.service.Padronizar import padronizarNome, padronizarEmail
from . import ValidatesTypes
from app.models import Discentes,db

@ValidatesTypes.TipagemEstaticaClasse
class AdiconarDiscentes:
    def __init__(self, discente: dict):
        self.discente = discente
        
    def validate(self):
        validates = ValidatesData(self.discente)
        validates.validate()
        return validates
    
    def salvar(self):
        discente = Discentes(**self.discente)
        discente.nome = padronizarNome(discente.nome)
        discente.email = padronizarEmail(discente.email)
        db.session.add(discente)
        db.session.commit()
        return discente.to_json()
        
    
        
        