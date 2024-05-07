# Importações do Flask, SQLAlchemy e LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# Importações do Python
import os

# Importações do projeto
from app.config.config import GlobalConfig

app = Flask(__name__)
app.config['SECRET_KEY'] = GlobalConfig.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = GlobalConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = GlobalConfig.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

# Cria a pasta UPLOAD_FOLDER se não existir
UPLOAD_FOLDER = GlobalConfig.UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Define a view para redirecionar usuários não autenticados

@login_manager.user_loader
def load_user(user_id):
    from app.models.models import User
    return User.query.get(user_id)

from app.routes import error, auth, home, product  # Importa as rotas após a criação do app para evitar importações circulares

app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)
app.register_blueprint(product.bp)
app.register_blueprint(error.bp)