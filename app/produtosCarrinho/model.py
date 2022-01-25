from app.extensions import db


# ProdutosCarrinho
# tabela que contem os produtos colocados no carrinho pelo usuário
# id => chave primária
# quantidade => quantidade de produtos colocados no carrinho 
# preco_total => preço total de todos as produtos colocados 

class ProdutosCarrinho(db.Model):
        __tablename__ = 'ProdutosCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # produtos carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # produtos(one) <-> produtos carrinho(many)
        produtos_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))

        def json(self):
                return{
                'quantidade':self.quantidade,
                'preco_total':self.preco_total
                }