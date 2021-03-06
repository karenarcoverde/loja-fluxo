from flask import Blueprint

from app.novidades.controller import NovidadesDetalhes, NovidadesId

novidades_api = Blueprint('novidades_api', __name__)

novidades_api.add_url_rule(
    '/novidades', view_func= NovidadesDetalhes.as_view('novidades_detalhes'), methods=['GET','POST']
)

novidades_api.add_url_rule(
    '/novidades/<int:id>', view_func= NovidadesId.as_view('novidades_id'), methods=['GET','PUT', 'PATCH','DELETE']
)