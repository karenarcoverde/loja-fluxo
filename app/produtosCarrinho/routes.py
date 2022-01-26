from flask import Blueprint

from app.produtosCarrinho.controller import ProdutosCarrinhoDetalhes

produtoscarrinho_api = Blueprint('produtoscarrinho_api', __name__)

produtoscarrinho_api.add_url_rule(
    '/produtoscarrinho', view_func= ProdutosCarrinhoDetalhes.as_view('produtoscarrinho_detalhes'), methods=['GET','POST']
)