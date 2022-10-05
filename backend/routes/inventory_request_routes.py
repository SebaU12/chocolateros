from flask import Blueprint
from controllers.inventory_requestController import create_request, list_request, update_request

inventory_request_blueprint = Blueprint('blueprint_irequest', __name__)

inventory_request_blueprint.route('/create_request', methods=['POST'])(create_request)
inventory_request_blueprint.route('/get_all', methods=['GET'])(list_request)
inventory_request_blueprint.route('/confirm/<id>', methods=['PUT'])(update_request)
