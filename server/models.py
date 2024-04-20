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
    role = db.Column(Enum('admin', 'student', 'enrollee', 'moderator', name='user_role'), default='enrollee')
    is_verified = db.Column(db.Boolean, default=False)


class Corps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=True)
    floors = relationship('Floor', backref='corps', lazy=True)  # Отношение к этажам


class Floor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    audiences = relationship('Audience', backref='floor', lazy=True)  # Отношение к аудиториям
    corps_id = db.Column(db.Integer, db.ForeignKey('corps.id'), nullable=False)  # Внешний ключ к Corps


class Audience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    type = db.Column(Enum('kabinet', 'labs', 'administration', 'sportzal', name='audience_type'), nullable=False)  # Использование Enum
    image_url = db.Column(db.String(500), nullable=False)
    floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'), nullable=False)  # Внешний ключ к Floor


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    region = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    site_url = db.Column(db.String(500), nullable=False)
    students_num = db.Column(db.Integer, nullable=False)
    budget_num = db.Column(db.Integer, nullable=False)  # Кол-во бюджетных мест
    teacher_num = db.Column(db.Integer, nullable=False)  # Кол-во преподавателей
    edprogram_num = db.Column(db.Integer, nullable=False)  # Кол-во образовательных программ
    branches_num = db.Column(db.Integer, nullable=False)  # Кол-во филиалов
    corp_num = db.Column(db.Integer, nullable=False)  # Кол-во корпусов
    faculty_num = db.Column(db.Integer, nullable=False)  # Кол-во факультетов
    departament_num = db.Column(db.Integer, nullable=False)  # Кол-во кафедр
    profession_classes_num = db.Column(db.Integer, nullable=False)  # Кол-во проф.классов
    dormitory_num = db.Column(db.Integer, nullable=False)  # Кол-во общежитий
    graduates_num = db.Column(db.Integer, nullable=False)  # Кол
    created_by_id = db.Column(db.Integer, nullable=False)


# создание кабинета, обновление кабинта, получение всех кабинетов и одного
# выдать все этажи корпуса и все кабинета этажа
