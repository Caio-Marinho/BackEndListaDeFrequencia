from flask_sqlalchemy import SQLAlchemy  # Biblioteca para interação com o banco de dados

db = SQLAlchemy() # Initializa SQLAlchemy

__all__ = ['db']