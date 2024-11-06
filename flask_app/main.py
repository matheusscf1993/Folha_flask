# flask_app/main.py
from flask import Flask
from database.session import db
from routes.routes import register_routes
from settings.config import create_app

app = create_app()  # Cria o aplicativo Flask com a configuração

# Inicializando o banco de dados
with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados, se ainda não existirem.

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
