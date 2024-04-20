import os
from datetime import timedelta


class FlaskAppConfig:
    APP_SECRET_KEY = os.getenv('APP_SECRET_KEY', '02078b9e402d62749310cab8ead4c99ef4f3970beaae898a')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE', 'sqlite:///yourdatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    UPLOAD_FOLDER = 'static'  # Путь к папке, куда будут сохраняться изображения голосований


class FlaskMailConfig:
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    SENDER = os.getenv('SENDER', 'your-email@example.com')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'testMail@corp.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', 'Oy7m4LwP1FGAfTJYQ8AqdQ==')


class UserConfig:
    MAX_STRING_LENGTH = 50
    MIN_PASSWORD_LENGTH = 8


