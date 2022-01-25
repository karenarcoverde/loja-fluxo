from flask import Flask
from app.config import Config
from app.extensions import db, migrate

from app.usuario.model import Usuario
from app.novidades.model import Novidades
from app.carrinho.model import Carrinho
from app.novidadesCarrinho.model import NovidadesCarrinho
from app.cupons.model import Cupons
from app.produtos.model import Produtos
from app.produtosCarrinho.model import ProdutosCarrinho

# cria o app
def create_app():
    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)
    migrate.init_app(app,db)

    return app