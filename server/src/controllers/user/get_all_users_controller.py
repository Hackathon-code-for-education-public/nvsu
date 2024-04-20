from flask import Blueprint, jsonify
from server.models import User

get_all_users_blueprint = Blueprint('getAllUsers', __name__)
get_user_blueprint = Blueprint('getUser', __name__)


@get_all_users_blueprint.route('/user/', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'surname': user.surname,
            'father_name': user.father_name,
            'email': user.email,
            'is_email_confirmed': user.is_email_confirmed
        }
        users_list.append(user_data)

    return jsonify(users_list)


@get_user_blueprint.route('/user/int:<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_data = {
        'id': user.id,
        'first_name': user.first_name,
        'surname': user.surname,
        'father_name': user.father_name,
        'email': user.email,
        'is_email_confirmed': user.is_email_confirmed
    }

    return jsonify(user_data)
