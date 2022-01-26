from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.novidadesCarrinho.model import NovidadesCarrinho

class NovidadesCarrinhoDetalhes(MethodView): 
    def get(self):
        novidadescarrinho = NovidadesCarrinho.query.all()
        return jsonify([novidadecarrinho.json() for novidadecarrinho in novidadescarrinho]),200

    def post(self):
        dados = request.json        
        nome_novidade = dados.get('nome_novidade')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')
       
        preco_total = quantidade * preco_unitario
       
        if isinstance (nome_novidade,str) and isinstance (quantidade,int) and isinstance (preco_unitario,int) and isinstance (preco_total,int):
            novidadecarrinho = NovidadesCarrinho(nome_novidade= nome_novidade, quantidade = quantidade, preco_unitario = preco_unitario, preco_total = preco_total)
            db.session.add(novidadecarrinho)
            db.session.commit()
            return novidadecarrinho.json(),200
        return {"code_status":"invalid data in request"},400

class NovidadesCarrinhoId(MethodView):
    def get (self,id):
        novidadecarrinho = NovidadesCarrinho.query.get_or_404(id)
        return novidadecarrinho.json()

    def put (self,id):
        dados = request.json
        nome_novidade = dados.get('nome_novidade')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')


        novidadecarrinho = NovidadesCarrinho.query.get_or_404(id)
        novidadecarrinho.nome_novidade = nome_novidade
        novidadecarrinho.quantidade = quantidade
        novidadecarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return novidadecarrinho.json(),200
      

    def patch (self,id):
        dados = request.json
        novidadecarrinho= NovidadesCarrinho.query.get_or_404 (id)
  
        nome_novidade= dados.get('nome_novidade',NovidadesCarrinho.nome_novidade)
        quantidade = dados.get('quantidade', NovidadesCarrinho.quantidade)
        preco_unitario = dados.get('preco_unitario',NovidadesCarrinho.preco_unitario)
     

        novidadecarrinho.nome_novidade = nome_novidade
        novidadecarrinho.quantidade = quantidade
        novidadecarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return novidadecarrinho.json(),200
    

    def delete(self,id):
        novidadecarrinho = NovidadesCarrinho.query.get_or_404(id)
        db.session.delete (novidadecarrinho)
        db.session.commit ()
        return {"code_status":"deletado"},200

