from flask import Blueprint, jsonify, request
#from datatables.user import User
#from datatables.database import db

import datatables.database as db

exampleBlueprint = Blueprint('exampleBlueprint', __name__)

@exampleBlueprint.route('/select0', methods=['GET'])
def select0():
    return jsonify(db.select(0))

@exampleBlueprint.route('/select1', methods=['GET'])
def select1():
    return jsonify(db.select(1))

@exampleBlueprint.route('/select2', methods=['GET'])
def select2():
    return jsonify(db.select(2))

@exampleBlueprint.route('/select3', methods=['GET'])
def select3():
    return jsonify(db.select(3))

@exampleBlueprint.route('/select4', methods=['GET'])
def select4():
    return jsonify(db.select(4))

@exampleBlueprint.route('/select5', methods=['GET'])
def select5():
    return jsonify(db.select(5))

@exampleBlueprint.route('/select6', methods=['GET'])
def select6():
    return jsonify(db.select(6))

@exampleBlueprint.route('/select7', methods=['GET'])
def select7():
    return jsonify(db.select(7))

@exampleBlueprint.route('/select8', methods=['GET'])
def select8():
    return jsonify(db.select(8))

@exampleBlueprint.route('/insert-employee', methods=['GET']) # http://127.0.0.1:5000/insert-employee?name=&surname=&patronymic=&job=
def insert_employee():
    name = request.args.get('name')
    surname = request.args.get('surname')
    patronymic = request.args.get('patronymic')
    job_title_id = request.args.get('job')
    db.insert_employment(name, surname, patronymic, job_title_id)
    
    return jsonify("True")

@exampleBlueprint.route('/get-employee-data', methods=['GET']) # http://127.0.0.1:5000/get-employee-data
def get_employee_data():
    name = request.args.get('name')
    surname = request.args.get('surname')
    patronymic = request.args.get('patronymic')
    job_title_id = request.args.get('job')
    
    return jsonify(db.get_employment_table())

@exampleBlueprint.route('/get-timetable', methods=['GET']) # http://127.0.0.1:5000/get-timetable
def get_timetable():
    return jsonify(db.get_timetable())


@exampleBlueprint.route('/delete-employee', methods=['GET']) # http://127.0.0.1:5000/delete-employee?id=
def delete_employee():
    id = request.args.get('id')
    db.delete_employment(id)
    return jsonify("True")

#@exampleBlueprint.route('/init_db', methods=['GET'])
#def init_database():
#
#    admin = User('admin', 'admin@example.com')
#    print("Data init:")
#    print(admin)
#    db.session.add(admin)
#    db.session.commit()
#
#    return jsonify('Init Database!')
#    None

#@exampleBlueprint.route('/get_db', methods=['GET'])
#def get_database():
#    data = User.query.all()
#    return jsonify(data[0].username)
#    None