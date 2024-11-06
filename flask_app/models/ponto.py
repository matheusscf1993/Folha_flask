from database.session import db
from datetime import datetime

class Ponto(db.Model):
    __tablename__ = 'pontos'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    horario_entrada = db.Column(db.DateTime, nullable=True)
    horario_saida = db.Column(db.DateTime, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Ajustado para usar datetime.utcnow
    action = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Ponto {self.usuario} - Entrada: {self.horario_entrada}, Saída: {self.horario_saida}>'
