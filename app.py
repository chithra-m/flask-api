from flask import Flask, request
# from database import db 
# from flask_sqlalchemy import SQLAlchemy
import logging 
from db_setup import create_app, db
from service import getUserData, postUserData,  putUser, deleteUser

logging.basicConfig(filename='record.log', level=logging.DEBUG) 

app = create_app()
with app.app_context():
    db.create_all()
app.logger.info('DB tables created')


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/user',methods=['GET'])
@app.route('/user/<id>',methods=['GET'])
def read_user(id=None):
    return getUserData(id)

@app.route('/user',methods=['POST'])
def insert_user():
    return postUserData(request.data)

@app.route('/user',methods=['PUT'])
def update_user():
    return putUser(request.data)

@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    return deleteUser(id)

if __name__ == '__main__':
    app.run(debug=True)