import logging
from flask import current_app
from server.src.crypto.hash import hashing, compare_hashes
from flask import Blueprint, request, jsonify, session
from server.models import db, User
from sqlalchemy.exc import SQLAlchemyError
from server.src.utils.data_validation import UserRegistrationSchema
from server.src.utils.email_utils.email_verifier import generate_confirmation_token, send_confirmation_email, confirm_token

# Настройка логгера
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Создаем Blueprint-ов для регистрации, авторизации и выхода из аккаунта
registration_blueprint = Blueprint('registrationBlueprint', __name__)
login_blueprint = Blueprint('loginBlueprint', __name__)
logout_blueprint = Blueprint('logoutBlueprint', __name__)


# Endpoint для регистрации
@registration_blueprint.route('/registration', methods=['POST'])
def registration():
    try:
        request_data = request.get_json()

        # Валидация данных
        errors = UserRegistrationSchema().validate(request_data)
        if errors:
            return jsonify(errors), 400

        validated_data = UserRegistrationSchema().load(request_data)

        # Проверка на существование пользователя по email
        user = User.query.filter(User.email == validated_data['email']).first()
        if user:
            return jsonify({'message': 'User already exist'}), 409

        # Хеширование пароля
        hashed_password = hashing(validated_data['password'])

        new_user = User(first_name=validated_data['first_name'],
                        surname=validated_data['surname'],
                        father_name=validated_data.get('father_name'),
                        email=validated_data['email'],
                        password=hashed_password.decode('utf-8'))  # Сохраняем декодированный хеш пароля

        db.session.add(new_user)  # Добавляем нового пользователя в сессию
        db.session.commit()  # Сохраняем изменения в базе данных

        token = generate_confirmation_token(validated_data['email'])
        new_user.email_confirm_token = token
        db.session.commit()
        # send_confirmation_email(validated_data['email'], token)
        print(token)

        return jsonify({'message': 'User was created successfuly'}), 201
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy Error: {e}")
        return jsonify({'message': 'Unknown error'}), 500  # Ошибка БД, но не сообщаем об этом пользователю явно
    except Exception as e:
        logger.error(f"General Error: {e}")
        return jsonify({'message': 'Error processing request'}), 500


@registration_blueprint.route('/confirm/<token>', methods=['GET'])
def confirm_email(token):
    try:
        email = confirm_token(token)
        if not email:
            # Если confirm_token вернул False, значит токен неверен или истек
            user = User.query.filter_by(email_confirm_token=token).first()  # Вытаскиваем инфу по пользователю на основании истекшего токена
            if user:
                new_token = generate_confirmation_token(user.email)
                print(new_token)
                user.email_confirm_token = new_token
                db.session.commit()
                send_confirmation_email(user.email, new_token)
                return jsonify({'message': 'The confirmation link is invalid or the link has expired. '
                                           'A new confirmation link has been sent to your email.'}), 400
            else:
                return jsonify({'message': 'User is not found'}), 404

        user = User.query.filter_by(email=email).first_or_404()

        if user.is_email_confirmed:
            return jsonify({'message': 'The account has already been verified'}), 200
        else:
            user.is_email_confirmed = True
            db.session.commit()
            return jsonify({'message': 'You have successfully verified your email'}), 200

    except Exception as e:
        # Логирование любых других ошибок
        current_app.logger.error(f'Error confirming email: {e}')
        return jsonify({'message': 'Internal Server Error'}), 500


# Endpoint для авторизации
@login_blueprint.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        email = request_data.get('email')
        password = request_data.get('password')

        if not email or not password:
            return jsonify({'message': 'You must provide an email and password'}), 400

        user = User.query.filter_by(email=email).first()

        if not user or not compare_hashes(password.encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({'message': 'Invalid email or password'}), 401

        # Устанавливаем user_id в сессии после успешной аутентификации
        session['user_id'] = user.id

        return jsonify({'message': 'Successful authorization'}), 200

    except Exception as e:
        logger.error(f"General Error: {e}")
        return jsonify({'message': 'Error processing request'}), 500


# Endpoint для выхода из учетной записи
@logout_blueprint.route('/logout', methods=['POST'])
def logout():
    # Удаляем user_id из сессии для выхода пользователя
    session.pop('user_id', None)
    return jsonify({'message': 'You have successfully logged out'}), 200
