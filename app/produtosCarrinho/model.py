from app.extensions import db


# ProdutosCarrinho
# tabela que contem os produtos colocados no carrinho pelo usuário
# id => chave primária
# quantidade => quantidade de produtos colocados no carrinho 
# preco_unitario => preço de somente um produto colocado no carrinho
# preco_total => preço total de todos as produtos colocados 

class ProdutosCarrinho(db.Model):
        __tablename__ = 'ProdutosCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        nome_produto = db.Column(db.String(20), nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # produtos carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # produtos(one) <-> produtos carrinho(many)
        produtos_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))

        def json(self):
                return{
                'nome_produto':self.nome_produto,
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }