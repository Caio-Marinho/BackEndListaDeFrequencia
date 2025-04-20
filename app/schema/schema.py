from . import schema
from app.models import Discentes, db

class DiscenteSchema(schema.SQLAlchemyAutoSchema):
    class Meta:
        model:type = Discentes
        load_instance = True
        sqla_session = db.session
        
    id = schema.auto_field(dump_only=True)
    email = schema.auto_field(required=True)
    horas = schema.auto_field(required=False)
    dias = schema.auto_field(required=False)
    categoria = schema.auto_field(required=True)
    
    @schema.validates('email')
    def email_valido(cls, email):
        if not email.endswith('@ufpe.br'):
            raise ValueError('Email precisa ser um dominio @ufpe.br')
        return email