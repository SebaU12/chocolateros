from flask import Blueprint
from controllers.record_ventasController import post_record, list_records 

record_blueprint = Blueprint('blueprint_ventas', __name__)

record_blueprint.route('/post_ventas', methods=['POST'])(post_record)
record_blueprint.route('/get_all', methods=['GET'])(list_records)
