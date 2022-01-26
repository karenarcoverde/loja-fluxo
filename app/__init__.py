from flask import Flask
from app.config import Config
from app.extensions import db, migrate

# models
from app.usuario.model import Usuario
from app.novidades.model import Novidades
from app.carrinho.model import Carrinho
from app.novidadesCarrinho.model import NovidadesCarrinho
from app.cupons.model import Cupons
from app.produtos.model import Produtos
from app.produtosCarrinho.model import ProdutosCarrinho

# routes
from app.usuario.routes import usuario_api

# cria o app
def create_app():
    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)
    migrate.init_app(app,db)

    # rotas implementadas
    app.register_blueprint(usuario_api)

    return app