
from app.globals import date, time
from app.models.models import Discentes
from app.models import db
from . import ma


class DiscenteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model:type = Discentes
        load_instance = True
        sqla_session = db.session
        
    id:int = ma.auto_field(dump_only=True)
    nome:str = ma.auto_field(required=True)
    email:str = ma.auto_field(required=True)
    data:date = ma.auto_field(dump_only=True)
    hora:time = ma.auto_field(dump_only=True)
    categoria:str = ma.auto_field(required=True)
