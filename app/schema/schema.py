from datetime import date,time
from . import schema
from app.models import Discentes, db

class DiscenteSchema(schema.SQLAlchemyAutoSchema):
    class Meta:
        model:type = Discentes
        load_instance = True
        sqla_session = db.session
        
    id:int = schema.auto_field(dump_only=True)
    nome:str = schema.auto_field(required=True)
    email:str = schema.auto_field(required=True)
    data:date = schema.auto_field(dump_only=True)
    hora:time = schema.auto_field(dump_only=True)
    categoria:str = schema.auto_field(required=True)
