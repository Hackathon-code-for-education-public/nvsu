from flask import Blueprint, jsonify, request, session
from server.models import db, Corps, Floor, Audience


corps_creation_blueprint = Blueprint('corps_creation', __name__)
create_floor_blueprint = Blueprint('create_floor', __name__)
create_audience_blueprint = Blueprint('create_audience', __name__)

# Проверка авторизации пользователя


def is_user_authenticated():
    return 'user_id' in session


@corps_creation_blueprint.route('/create_corps', methods=['POST'])
def create_corps():
    if not is_user_authenticated():
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    new_corps = Corps(name=data['name'], image_url=data['image_url'], description=data.get('description', ''))
    db.session.add(new_corps)
    db.session.commit()
    return jsonify({'message': 'Corps created successfully'}), 201


@create_floor_blueprint.route('/create_floor', methods=['POST'])
def create_floor():
    if not is_user_authenticated():
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    new_floor = Floor(num=data['num'], image_url=data['image_url'], corps_id=data['corps_id'])
    db.session.add(new_floor)
    db.session.commit()
    return jsonify({'message': 'Floor created successfully'}), 201


@create_audience_blueprint.route('/create_audience', methods=['POST'])
def create_audience():
    if not is_user_authenticated():
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    new_audience = Audience(num=data['num'], type=data['type'], image_url=data['image_url'], floor_id=data['floor_id'])
    db.session.add(new_audience)
    db.session.commit()
    return jsonify({'message': 'Audience created successfully'}), 201


