from flask import Blueprint

from app.novidadesCarrinho.controller import NovidadesCarrinhoDetalhes, NovidadesCarrinhoId

novidadescarrinho_api = Blueprint('novidadescarrinho_api', __name__)

novidadescarrinho_api.add_url_rule(
    '/novidadescarrinho', view_func= NovidadesCarrinhoDetalhes.as_view('novidadescarrinho_detalhes'), methods=['GET','POST']
)

novidadescarrinho_api.add_url_rule(
    '/novidadescarrinho/<int:id>', view_func= NovidadesCarrinhoId.as_view('novidadescarrinho_id'), methods=['GET','PUT', 'PATCH','DELETE']
)