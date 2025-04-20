
from . import db
from datetime import date

class Discentes(db.Model):
    # Definindo as colunas do banco de dados com nomes explícitos
    id:int = db.Column(db.Integer, primary_key=True)
    nome:str = db.Column(db.String(100), nullable=False)
    email:str = db.Column(db.String(100), nullable=False, unique=True)
    data:date = db.Column(db.Date, default=date.today())
    categoria:str = db.Column(db.String(100), nullable=False)

    def __init__(self, nome:str, email:str, categoria:str):
        self.nome:str = nome
        self.email:str = email
        self.categoria:str = categoria
        
    def getnome(self):
        return self.nome

    def getemail(self):
        return self.email

    def getcategoria(self):
        return self.categoria

    def setnome(self, nome):
        self.nome = nome
    
    def setemail(self, email):
        self.email = email
    
    def setcategoria(self, categoria):
        self.categoria = categoria
    
    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'data': self.data.strftime('%Y/%m/%d'),
            'categoria': self.categoria
        }
