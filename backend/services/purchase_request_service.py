from flask import jsonify, request
import database as db_config
from models.purchase_request import PRequest, prequest_schema, prequests_schema

db = db_config.db_sql

def send_request():
    amount = request.json['amount']
    supplier = request.json['supplier']
    request_date = request.json['request_date']
    motive = request.json['motive']
    purchase_request = PRequest(amount, supplier, 
            request_date, motive)
    db.session.add(purchase_request)
    db.session.commit()
    return prequest_schema.jsonify(purchase_request) 

def get_requests(): 
    all_request = PRequest.query.all()
    result = prequests_schema.dump(all_request)
    return jsonify(result)

def update_state(id):
    prequest = PRequest.query.get(id)
    prequest.state = True
    db.session.commit()
    return prequest_schema.jsonify(prequest)

