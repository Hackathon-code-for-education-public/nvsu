from flask import Blueprint, request, jsonify, session
from models import db, University

update_university_blueprint = Blueprint('update_university', __name__)


@update_university_blueprint.route('/universities/edit/<int:university_id>', methods=['GET', 'POST'])
def edit_university(university_id):
    if 'user_id' not in session:
        return jsonify({'message': 'User not authenticated'}), 401

    user_id = session['user_id']
    university = University.query.get_or_404(university_id)

    if university.created_by_id != user_id:
        return jsonify({'message': 'User not authorized to edit this university'}), 403

    if request.method == 'POST':
        university.name = request.form['name']
        university.description = request.form['description']
        university.region = request.form['region']
        university.city = request.form['city']
        university.image_url = request.form['image_url']
        university.email = request.form['email']
        university.phone = request.form['phone']
        university.address = request.form['address']
        university.site_url = request.form['site_url']
        university.students_num = request.form['students_num']
        university.budget_num = request.form['budget_num']
        university.teacher_num = request.form['teacher_num']
        university.edprogram_num = request.form['edprogram_num']
        university.branches_num = request.form['branches_num']
        university.corp_num = request.form['corp_num']
        university.faculty_num = request.form['faculty_num']
        university.departament_num = request.form['departament_num']
        university.profession_classes_num = request.form['profession_classes_num']
        university.dormitory_num = request.form['dormitory_num']
        db.session.commit()
        return jsonify({'message': 'University information successfully updated'})

    # Если метод GET, можно вернуть сообщение о том, что метод не поддерживается для данного URL
    return jsonify({'message': 'Use POST method to edit university'}), 405
