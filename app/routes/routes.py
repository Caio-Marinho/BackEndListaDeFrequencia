from app.globals import Blueprint
from app.view import index_view

routes = Blueprint('routes', __name__)


routes.add_url_rule('/', view_func=index_view, methods=['GET','POST'])
