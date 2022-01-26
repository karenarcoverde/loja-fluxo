from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.produtosCarrinho.model import ProdutosCarrinho

class ProdutosCarrinhoDetalhes(MethodView): 
    def get(self):
        produtoscarrinho = ProdutosCarrinho.query.all()
        return jsonify([produtocarrinho.json() for produtocarrinho in produtoscarrinho]),200

    def post(self):
        dados = request.json        
        nome_produto = dados.get('nome_produto')
        quantidade = dados.get('quantidade')
        preco_total = dados.get('preco_total')
       
        if isinstance (nome_produto,str) and isinstance (quantidade,int) and isinstance (preco_total,int):
            produtocarrinho = ProdutosCarrinho(nome_produto= nome_produto, quantidade = quantidade, preco_total = preco_total)
            db.session.add(produtocarrinho)
            db.session.commit()
            return produtocarrinho.json(),200
        return {"code_status":"invalid data in request"},400