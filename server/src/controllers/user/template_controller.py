# В экстренном случае - переименовать название файла

from flask import Blueprint, jsonify
from server.models import db, Template

creating_template_controller = Blueprint('template_controller', __name__)
get_all_templates_controller = Blueprint('get_all_templates_controller', __name__)


@creating_template_controller.route('/template/', methods=['GET'])
def create_template():
    pass


@get_all_templates_controller.route('/template/', methods=['GET'])
def get_all_templates():
    pass


