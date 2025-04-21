from . import db
from datetime import datetime, date, time
import pytz
import os

class Discentes(db.Model):
    """
    Modelo de dados para os discentes.

    Attributes:
        id (int): ID do discente.
        nome (str): Nome do discente.
        email (str): Email do discente.
        data (date): Data de cadastro do discente.
        hora (time): Hora de cadastro do discente.
        categoria (str): Categoria do discente.
    """
    # Use a variável de ambiente TIMEZONE, ou padrão para UTC
    regiao = os.getenv('TIMEZONE', 'America/Recife')
    
    # Funções auxiliares
    # Função para obter a data e hora atual na região especificada
    def get_date():
        return datetime.now(pytz.timezone(Discentes.regiao)).date()

    def get_time():
        return datetime.now(pytz.timezone(Discentes.regiao)).time()
    
    # Definindo as colunas do banco de dados com nomes explícitos
    id: int = db.Column(db.Integer, primary_key=True) # Chave primária
    nome: str = db.Column(db.String(100), nullable=False) # Nome do discente
    email: str = db.Column(db.String(100), nullable=False) # Email do discente
    data: date = db.Column(db.Date, default=get_date, nullable=False) # Data de cadastro
    hora:time = db.Column(db.Time, default=get_time, nullable=False) # Hora de cadastro
    categoria: str = db.Column(db.String(100), nullable=False) # Categoria do discente

    def __init__(self, nome: str, email: str, categoria: str) -> None:
        """
        Inicializa o modelo de dados com os dados do discente.

        Args:
            nome (str): Nome do discente.
            email (str): Email do discente.
            categoria (str): Categoria do discente.

        Returns:
            None
        """
        self.nome: str = nome
        self.email: str = email
        self.categoria: str = categoria

    def getnome(self) -> str:
        """
        Retorna o nome do discente.

        Returns:
            str: Nome do discente.
        """
        return self.nome

    def getemail(self) -> str:
        """
        Retorna o email do discente.

        Returns:
            str: Email do discente.
        """
        return self.email

    def getcategoria(self) -> str:
        """
        Retorna a categoria do discente.

        Returns:
            str: Categoria do discente.
        """
        return self.categoria

    def setnome(self, nome: str) -> None:
        """
        Define o nome do discente.

        Args:
            nome (str): Nome do discente.

        Returns:
            None
        """
        self.nome = nome

    def setemail(self, email: str) -> None:
        """
        Define o email do discente.

        Args:
            email (str): Email do discente.

        Returns:
            None
        """
        self.email = email

    def setcategoria(self, categoria: str) -> None:
        """
        Define a categoria do discente.

        Args:
            categoria (str): Categoria do discente.

        Returns:
            None
        """
        self.categoria = categoria

    def to_json(self) -> dict:
        """
        Retorna os dados do discente em formato JSON.

        Returns:
            dict: Dados do discente em formato JSON.
        """
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'data': self.data.strftime('%Y/%m/%d'),
            'hora': self.hora.strftime('%H:%M:%S'),
            'categoria': self.categoria
        }