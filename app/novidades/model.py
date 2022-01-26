from app.extensions import db

# Novidades
# tabela que contem as informações sobre todas novidades
# id => chave primária
# nome_produto => nome do produto cadastrado
# descricao => uma breve descricao sobre o produto, componentes utilizados nele etc.
# preco => preço do produto
# validade => validade do produto, em que não deve ser mais consumido
# data_lancamento => data que foi lançada no site.Já que está na categoria novidades, quer dizer que o produto é recente, então é interessante mostrar o quão recente
# ele é, pela data 

class Novidades(db.Model):
        __tablename__ = 'novidades'
        id = db.Column(db.Integer, primary_key = True)
        nome_novidade = db.Column(db.String(20), nullable = False)
        descricao = db.Column(db.String(50), nullable = False)
        preco = db.Column(db.Integer, nullable = False)
        validade = db.Column(db.String(10), nullable = False)
        data_lancamento = db.Column(db.String(10), nullable = False)

        # novidades(one) <-> novidades carrinho(many)
        novidades_carrinho = db.relationship('NovidadesCarrinho', backref = 'novidadesCarrinho')

        def json(self):
                return{
                'nome_novidade':self.nome_novidade,
                'descricao':self.descricao,
                'preco':self.preco,
                'validade':self.validade,
                'data_lancamento':self.data_lancamento
                }