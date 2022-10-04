from flask import Blueprint
from controllers.record_allController import post_record, list_records 

record_all_blueprint = Blueprint('blueprint_record', __name__)

record_all_blueprint.route('/post_record', methods=['POST'])(post_record)
record_all_blueprint.route('/get_all', methods=['GET'])(list_records)
