from flask import Blueprint
from controllers.purchase_requestController import create_request, list_request

purchase_request_blueprint = Blueprint('blueprint_request', __name__)

purchase_request_blueprint.route('/create_request', methods=['POST'])(create_request)
purchase_request_blueprint.route('/get_all', methods=['GET'])(list_request)
