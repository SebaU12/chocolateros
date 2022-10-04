import database as db_config
from services.record_all_service import add_record, get_records 

db=db_config.db_sql

def post_record():
    return add_record()

def list_records():
    return get_records()
