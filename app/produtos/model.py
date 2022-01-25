from app.extensions import db

# Produtos
# tabela que contem as informações sobre todos os produtos
# id => chave primária
# nome_produto => nome do produto cadastrado
# descricao => uma breve descricao sobre o produto, componentes utilizados nele etc.
# preco => preço do produto
# validade => validade do produto, em que não deve ser mais consumido

class Produtos(db.Model):
        __tablename__ = 'produtos'
        id = db.Column(db.Integer, primary_key = True)
        nome_produto = db.Column(db.String(20), nullable = False)
        descricao = db.Column(db.String(50), nullable = False)
        preco = db.Column(db.Integer, nullable = False)
        validade = db.Column(db.Integer, nullable = False)

        # produtos(one) <-> produtos carrinho(many)
        produtos_carrinho = db.relationship('ProdutosCarrinho', backref = 'produtosCarrinho')

        def json(self):
                return{
                'nome_produto':self.nome_produto,
                'descricao':self.descricao,
                'preco':self.preco,
                'validade':self.validade
                }