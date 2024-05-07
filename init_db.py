from app import app, db
from app.models.models import *  # Importa os modelos para garantir que eles estão disponíveis

def init_db():
    with app.app_context():  # Utiliza o contexto do aplicativo Flask existente
        db.create_all()  # Cria todas as tabelas no banco de dados

if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso!")
