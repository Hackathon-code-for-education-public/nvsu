from flask import Blueprint, jsonify
from models import User, db

delete_user_blueprint = Blueprint('deleteUser', __name__)


@delete_user_blueprint.route('/user/<int:user_id>', methods=['DELETE'])  # Используем int для параметра user_id
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)  # Используем db.session.delete() для удаления объекта
    db.session.commit()  # Фиксируем изменения в базе данных
    return jsonify({'message': 'User deleted'}), 200
