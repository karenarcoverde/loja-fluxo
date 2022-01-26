from flask import Blueprint

from app.novidadesCarrinho.controller import NovidadesCarrinhoDetalhes

novidadescarrinho_api = Blueprint('novidadescarrinho_api', __name__)

novidadescarrinho_api.add_url_rule(
    '/novidadescarrinho', view_func= NovidadesCarrinhoDetalhes.as_view('novidadescarrinho_detalhes'), methods=['GET','POST']
)
