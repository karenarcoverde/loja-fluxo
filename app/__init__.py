from flask import Flask
from app.config import Config
from app.extensions import db, migrate, mail, jwt

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
from app.carrinho.routes import carrinho_api
from app.cupons.routes import cupons_api
from app.novidades.routes import novidades_api
from app.produtos.routes import produtos_api
from app.novidadesCarrinho.routes import novidadescarrinho_api
from app.produtosCarrinho.routes import produtoscarrinho_api

# cria o app
def create_app():
    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)

    # rotas implementadas
    app.register_blueprint(usuario_api)
    app.register_blueprint(carrinho_api)
    app.register_blueprint(cupons_api)
    app.register_blueprint(novidades_api)
    app.register_blueprint(produtos_api)
    app.register_blueprint(novidadescarrinho_api)
    app.register_blueprint(produtoscarrinho_api)

    return app