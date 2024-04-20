from flask import Blueprint, jsonify, request, session
from sqlalchemy.exc import SQLAlchemyError

# Предполагается, что models и db уже импортированы
from models import db, Corps, Floor, Audience

corps_creation_blueprint = Blueprint('corps_creation', __name__)
create_floor_blueprint = Blueprint('create_floor', __name__)
create_audience_blueprint = Blueprint('create_audience', __name__)


def is_authenticated():
    """Проверяет, авторизован ли пользователь."""
    return 'user_id' in session


@corps_creation_blueprint.route('/corps', methods=['POST'])
def create_corps():
    if not is_authenticated():
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.get_json()
    try:
        new_corps = Corps(name=data['name'], image_url=data['image_url'], description=data.get('description'))
        db.session.add(new_corps)
        db.session.commit()
        return jsonify({'message': 'Corps created successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error', 'error': str(e)}), 500


@create_floor_blueprint.route('/floor', methods=['POST'])
def create_floor():
    if not is_authenticated():
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.get_json()
    try:
        new_floor = Floor(num=data['num'], image_url=data['image_url'], corps_id=data['corps_id'])
        db.session.add(new_floor)
        db.session.commit()
        return jsonify({'message': 'Floor created successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error', 'error': str(e)}), 500


@create_audience_blueprint.route('/audience', methods=['POST'])
def create_audience():
    if not is_authenticated():
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.get_json()
    try:
        new_audience = Audience(num=data['num'], type=data['type'], image_url=data['image_url'], floor_id=data['floor_id'])
        db.session.add(new_audience)
        db.session.commit()
        return jsonify({'message': 'Audience created successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error', 'error': str(e)}), 500
