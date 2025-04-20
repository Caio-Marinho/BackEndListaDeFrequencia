from . import db
from datetime import date

class Discentes(db.Model):
    # Definindo as colunas do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, default=date.today())
    horas = db.Column(db.String(50), nullable=False)
    dias = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, nome, email, horas, dias, categoria):
        self.nome = nome
        self.email = email
        self.horas = horas
        self.dias = dias
        self.categoria = categoria