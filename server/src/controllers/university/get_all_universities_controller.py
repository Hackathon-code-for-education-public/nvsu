from flask import Blueprint, request, jsonify
from models import University

get_all_universities_blueprint = Blueprint('get_all_universities', __name__)
get_university_blueprint = Blueprint('get_university', __name__)


@get_all_universities_blueprint.route('/universities/all', methods=['GET'])
def get_universities():
    # Получаем параметры страницы и размера из запроса, устанавливаем значения по умолчанию
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    try:
        # Используем пагинацию, предоставляемую SQLAlchemy
        pagination = University.query.paginate(page=page, per_page=per_page, error_out=False)
        universities = pagination.items

        # Преобразуем объекты университетов в словари для JSON-ответа
        universities_data = []
        for university in universities:
            universities_data.append({
                'id': university.id,
                'name': university.name,
                'description': university.description,
                'region': university.region,
                'city': university.city,
                'image': university.image_url,
                'email': university.email,
                'phone': university.phone,
                'address': university.address,
                'site_url': university.site_url,
                'students_num': university.students_num,
                'budget_num': university.budget_num,
                'teacher_num': university.teacher_num,
                'edprogram_num': university.edprogram_num,
                'branches_num': university.branches_num,
                'corp_num': university.corp_num,
                'faculty_num': university.faculty_num,
                'departament_num': university.departament_num,
                'profession_classes_num': university.profession_classes_num,
                'dormitory_num': university.dormitory_num
            })

        # Возвращаем список университетов и информацию о пагинации
        return jsonify({
            'universities': universities_data,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }), 200
    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500


@get_university_blueprint.route('/universities/<university_id>', methods=['GET'])
def get_user(university_id):
    university = University.query.get(university_id)
    if not university:
        return jsonify({'message': 'University not found'}), 404

    university_data = {
        'id': university.id,
        'name': university.name,
        'description': university.description,
        'region': university.region,
        'city': university.city,
        'image': university.image_url,
        'email': university.email,
        'phone': university.phone,
        'address': university.address,
        'site_url': university.site_url,
        'students_num': university.students_num,
        'budget_num': university.budget_num,
        'teacher_num': university.teacher_num,
        'edprogram_num': university.edprogram_num,
        'branches_num': university.branches_num,
        'corp_num': university.corp_num,
        'faculty_num': university.faculty_num,
        'departament_num': university.departament_num,
        'profession_classes_num': university.profession_classes_num,
        'dormitory_num': university.dormitory_num
        }

    return jsonify(university_data)
