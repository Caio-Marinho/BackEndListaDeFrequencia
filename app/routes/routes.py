from . import routes
from app.view.index import index_view

routes.add_url_rule('/', view_func=index_view, methods=['GET','POST'])