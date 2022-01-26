from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.produtos.model import Produtos

class ProdutosDetalhes(MethodView): 
    def get(self):
        produtos = Produtos.query.all()
        return jsonify([produto.json() for produto in produtos]),200

    def post(self):
        dados = request.json        
        nome_produto = dados.get('nome_produto')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        validade = dados.get('validade')

        if isinstance (nome_produto,str) and isinstance (descricao,str) and isinstance (preco,int) and isinstance (validade,str):
            produto = Produtos(nome_produto= nome_produto, descricao = descricao, preco = preco, validade = validade)
            db.session.add(produto)
            db.session.commit()
            return produto.json(),200
        return {"code_status":"invalid data in request"},400

class ProdutosId(MethodView):
    def get (self,id):
        produto = Produtos.query.get_or_404(id)
        return produto.json()

    def put (self,id):
        dados = request.json
        nome_produto = dados.get('nome_produto')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        validade = dados.get('validade')


        produto = Produtos.query.get_or_404(id)
        produto.nome_novidade = nome_produto
        produto.descricao = descricao
        produto.preco = preco
        produto.validade = validade

        db.session.commit()
        return produto.json(),200
      

    def patch (self,id):
        dados = request.json
        produto= Produtos.query.get_or_404 (id)
  
        nome_produto= dados.get('nome_produto',Produtos.nome_produto)
        descricao = dados.get('descricao', Produtos.descricao)
        preco = dados.get('preco',Produtos.preco)
        validade = dados.get('validade',Produtos.validade)

        produto.nome_produto = nome_produto
        produto.descricao = descricao
        produto.preco = preco
        produto.validade = validade
    
        db.session.commit()
        return produto.json(),200
    

    def delete(self,id):
        produto = Produtos.query.get_or_404(id)
        db.session.delete (produto)
        db.session.commit ()
        return {"code_status":"deletado"},200

