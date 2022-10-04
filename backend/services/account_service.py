from flask import jsonify, request
import database as db_config
from werkzeug.security import check_password_hash
from os import environ 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
db=db_config.dbConnection_mongo()

def login():
    req_username = request.json['username']
    req_password = request.json['password']
    if req_username and req_password: 
        accounts = db.accounts
        account = accounts.find_one({"username": req_username})
        if account:
            password = req_password + environ.get("SECRET_KEY") 
            if check_password_hash(account['password'], password):
                return jsonify({"message":"Logged in successfully"})
            return jsonify({"message":"Incorrect password"})
        return jsonify({"message":"Username does not exist on DB"})

