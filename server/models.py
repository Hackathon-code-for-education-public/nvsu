from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    father_name = db.Column(db.String(80), nullable=True)  # предполагаем, что отчество может быть не указано
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    #is_email_confirmed = db.Column(db.Boolean, default=False)
    #is_blocked = db.Column(db.Boolean, default=False)
    #email_confirm_token = db.Column(db.String(100))


class Corps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=True)
    floors = relationship('Floor', backref='corps', lazy=True)  # Добавляем отношение к этажам


class Floor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    audiences = relationship('Audience', backref='floor', lazy=True)  # Добавляем отношение к аудиториям


class Audience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    type = Enum('kabinet', 'labs', 'administration', 'sportzal', name='audience_type')  # узнать про enum
    image_url = db.Column(db.String(500), nullable=False)
    floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'), nullable=False)  # Внешний ключ к Floor


# создание кабинета, обновление кабинта, получение всех кабинетов и одного
# выдать все этажи корпуса и все кабинета этажа
