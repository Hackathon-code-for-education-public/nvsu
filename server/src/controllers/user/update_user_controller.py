from flask import Blueprint, request, jsonify, session
from models import User, db

update_user_blueprint = Blueprint('update_user', __name__)


@update_user_blueprint.route('/user/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    # Получаем ID авторизованного пользователя из сессии
    session_user_id = session.get('user_id')
    if not session_user_id:
        return jsonify({'error': 'Unauthorized access'}), 401

    # Проверяем соответствие ID пользователя из URL и ID пользователя из сессии
    if session_user_id != user_id:
        return jsonify({'error': 'Access denied'}), 403

    # Проверка наличия пользователя в базе данных
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    # Получение данных из запроса, если они есть
    first_name = data.get('first_name')
    surname = data.get('surname')
    father_name = data.get('father_name')
    email = data.get('email')

    # Проверка, что хотя бы одно поле было предоставлено для обновления
    if not any([first_name, surname, father_name, email]):
        return jsonify({'error': 'No data provided for update'}), 400

    # Обновление предоставленных данных пользователя
    if first_name is not None:
        user.first_name = first_name
    if surname is not None:
        user.surname = surname
    if father_name is not None:
        user.father_name = father_name
    if email is not None:
        user.email = email

    db.session.commit()

    return jsonify({'message': 'User data updated successfully'}), 200
