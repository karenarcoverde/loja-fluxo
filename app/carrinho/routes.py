from flask import Blueprint

from app.carrinho.controller import CarrinhoDetalhes

carrinho_api = Blueprint('carrinho_api', __name__)

carrinho_api.add_url_rule(
    '/carrinhos', view_func= CarrinhoDetalhes.as_view('carrinho_detalhes'), methods=['GET','POST']
)
