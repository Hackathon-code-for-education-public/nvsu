from flask import Flask
from flask_mail import Mail
from config import FlaskAppConfig, FlaskMailConfig
from models import db
from src.controllers.errors_controller import errorsBlueprint
from src.controllers.user.authentication_controller import registration_blueprint
from src.controllers.user.authentication_controller import login_blueprint
from src.controllers.user.authentication_controller import logout_blueprint
from src.controllers.user.get_all_users_controller import get_all_users_blueprint
from src.controllers.user.get_all_users_controller import get_user_blueprint
from src.controllers.user.delete_user_controller import delete_user_blueprint
from src.controllers.user.update_user_controller import update_user_blueprint
from src.controllers.sections.create_audience_controller import corps_creation_blueprint
from src.controllers.sections.create_audience_controller import create_floor_blueprint
from src.controllers.sections.create_audience_controller import create_audience_blueprint
from src.controllers.university.create_university_controller import create_university_blueprint
from src.controllers.university.get_all_universities_controller import get_all_universities_blueprint
from src.controllers.university.get_all_universities_controller import get_university_blueprint

mail = Mail()
app = Flask(__name__)
app.config.from_object(FlaskAppConfig)
app.config['SECRET_KEY'] = app.config['APP_SECRET_KEY']
app.config['SECURITY_PASSWORD_SALT'] = FlaskMailConfig.SECURITY_PASSWORD_SALT
app.config['UPLOAD_FOLDER'] = app.config['UPLOAD_FOLDER']


mail.init_app(app)
db.init_app(app)

app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(errorsBlueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(get_all_users_blueprint)
app.register_blueprint(get_user_blueprint)
app.register_blueprint(delete_user_blueprint)
app.register_blueprint(update_user_blueprint)

app.register_blueprint(corps_creation_blueprint)
app.register_blueprint(create_floor_blueprint)
app.register_blueprint(create_audience_blueprint)

app.register_blueprint(create_university_blueprint)
app.register_blueprint(get_all_universities_blueprint)
app.register_blueprint(get_university_blueprint)


def create_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    from models import *
    create_db()
    app.run(debug=True)
