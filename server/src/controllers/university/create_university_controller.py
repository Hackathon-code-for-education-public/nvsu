from flask import Blueprint, jsonify, request, session
from models import db, University


create_university_blueprint = Blueprint('create_university', __name__)


def is_authenticated():
    """Проверяет, авторизован ли пользователь."""
    return 'user_id' in session


@create_university_blueprint.route('/universities', methods=['POST'])
def create_university():
    data = request.get_json()

    if not all(key in data for key in ('name', 'description', 'region', 'city')):
        return jsonify({'message': 'Missing data'}), 400

    university = University(
        name=data['name'],
        description=data['description'],
        region=data['region'],
        city=data['city'],
        image_url=data.get('image_url'),
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        site_url=data['site_url'],
        students_num=data['students_num'],
        budget_num=data['budget_num'],
        teacher_num=data['teacher_num'],
        edprogram_num=data['edprogram_num'],
        branches_num=data['branches_num'],
        corp_num=data['corp_num'],
        faculty_num=data['faculty_num'],
        departament_num=data['departament_num'],
        profession_classes_num=data['profession_classes_num'],
        dormitory_num=data['dormitory_num'],
        graduates_num=data['graduates_num'],
        created_by_id=session['user_id']
    )

    try:
        db.session.add(university)
        db.session.commit()
        return jsonify({'message': 'University created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to create university', 'error': str(e)}), 500
