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
        preco_unitario = dados.get('preco_unitario')
      
        preco_total = quantidade * preco_unitario
       
        if isinstance (nome_produto,str) and isinstance (quantidade,int) and isinstance (preco_unitario,int) and isinstance (preco_total,int):
            produtocarrinho = ProdutosCarrinho(nome_produto= nome_produto, quantidade = quantidade, preco_unitario = preco_unitario, preco_total = preco_total)
            db.session.add(produtocarrinho)
            db.session.commit()
            return produtocarrinho.json(),200
        return {"code_status":"invalid data in request"},400

class ProdutosCarrinhoId(MethodView):
    def get (self,id):
        produtocarrinho = ProdutosCarrinho.query.get_or_404(id)
        return produtocarrinho.json()

    def put (self,id):
        dados = request.json
        nome_produto = dados.get('nome_produto')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')


        produtocarrinho = ProdutosCarrinho.query.get_or_404(id)
        produtocarrinho.nome_produto = nome_produto
        produtocarrinho.quantidade = quantidade
        produtocarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return produtocarrinho.json(),200
      

    def patch (self,id):
        dados = request.json
        produtocarrinho= ProdutosCarrinho.query.get_or_404 (id)
  
        nome_produto= dados.get('nome_produto',ProdutosCarrinho.nome_produto)
        quantidade = dados.get('quantidade', ProdutosCarrinho.quantidade)
        preco_unitario = dados.get('preco_unitario',ProdutosCarrinho.preco_unitario)
     

        produtocarrinho.nome_produto = nome_produto
        produtocarrinho.quantidade = quantidade
        produtocarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return produtocarrinho.json(),200
    

    def delete(self,id):
        produtocarrinho = ProdutosCarrinho.query.get_or_404(id)
        db.session.delete (produtocarrinho)
        db.session.commit ()
        return {"code_status":"deletado"},200

