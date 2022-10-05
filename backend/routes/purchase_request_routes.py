from flask import Blueprint
from controllers.purchase_requestController import create_request, list_request, update_request

purchase_request_blueprint = Blueprint('blueprint_prequest', __name__)

purchase_request_blueprint.route('/create_request', methods=['POST'])(create_request)
purchase_request_blueprint.route('/get_all', methods=['GET'])(list_request)
purchase_request_blueprint.route('/confirm/<id>', methods=['PUT'])(update_request)
