import database as db_config
from services.purchase_request_service import send_request, get_requests 

db=db_config.db_sql

def create_request():
    return send_request()

def list_request():
    return get_requests()
