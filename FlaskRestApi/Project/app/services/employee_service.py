from Project.app.models import Employee
from flask import jsonify
from bson import ObjectId
from bson.json_util import dumps


class EmployeeService:
    @staticmethod
    def add_employee(data, collection):
        empId = data.get('empId')
        empName = data.get('empName')
        empSalary = data.get('empSalary')
        empRole = data.get('empRole')
        if empId and empName and empSalary and empRole:
            try:
                exiting_record = collection.find_one({'empId': empId})
                if exiting_record:
                    return jsonify({'status': '1', 'error': f'This Employee Id:{empId} already exists.'})
                else:
                    collection.insert_one({'empId': empId, 'empName': empName, 'empSalary': empSalary, 'empRole': empRole})
                    return jsonify({'empId': empId, 'empName': empName, 'empSalary': empSalary, 'empRole': empRole,
                                    'status': '0',
                                    'message': 'Employee Record added successfully!',
                                    'status_code': f'{200}'})
            except Exception as e:
                return jsonify({'status': '1', 'message': f'{e}'})
        return jsonify({'message': 'All fields should be given'})

    @staticmethod
    def get_employees(collection):
        try:
            allEmployee = collection.find()
            # dump() function in Python allows you to store JSON data directly into a file
            # result = dumps(allEmployee)
            if allEmployee:
                result = []
                for employee in allEmployee:
                    result.append({
                        '_id': str(employee['_id']),
                        'empId': employee['empId'],
                        'empName': employee['empName'],
                        'empRole': employee['empRole'],
                        'empSalary': employee['empSalary']
                    })
                return result
            return jsonify({'message': 'No Record Found', 'status': '1', 'status_code': f'{400}'})
        except Exception as e:
            return jsonify({'status': '1', 'message': f'{e}'})

    @staticmethod
    def get_employee(collection, Id):
        try:
            object_id = ObjectId(Id)
            employee = collection.find_one({'_id': object_id})
            if employee:
                result = {
                    '_id': str(employee['_id']),
                    'empId': employee['empId'],
                    'empName': employee['empName'],
                    'empRole': employee['empRole'],
                    'empSalary': employee['empSalary']
                }
                return jsonify(result)
            else:
                return jsonify({'message': f'This employee:{Id} not in db', 'status': '1', 'status_code': f'{404}'})
        except Exception as e:
            return jsonify({'status': '1', 'message': f'{e}'})

    @staticmethod
    def update_employee(data, collection, Id):
        try:
            object_id = ObjectId(Id)
            employee = collection.find_one({'_id': object_id})
            if employee:
                empId = data.get('empId')
                empName = data.get('empName')
                empSalary = data.get('empSalary')
                empRole = data.get('empRole')
                updated_record = {
                    '$set': {
                        'empId': empId,
                        'empName': empName,
                        'empSalary': empSalary,
                        'empRole': empRole
                    }
                }
                updated_record = collection.update_one({'_id': object_id}, updated_record)
                if updated_record:
                    return jsonify({'message': f'This {object_id} is updated!',
                                    'status': '0', 'status_code': f'{200}'})
                return jsonify({'message': f'This employee:{object_id} not in db', 'status': '1', 'status_code': f'{404}'})
        except Exception as e:
            return jsonify({'status': '1', 'message': f'{e}'})

    @staticmethod
    def remove_employee(collection, Id):
        try:
            object_id = ObjectId(Id)
            employee = collection.find_one({'_id': object_id})
            if employee:
                collection.delete_one({'_id': object_id})
                return jsonify({'message': f'This employee:{object_id} is deleted successfully!',
                                'status': '0', 'status_code': f'{200}'})
            return jsonify({'message': f'This employee:{object_id} not in db', 'status': '1', 'status_code': f'{404}'})
        except Exception as e:
            return jsonify({'status': '1', 'message': f'{e}'})

    @staticmethod
    def search_text(collection, search_query):

        if not search_query:
            return jsonify({'message': 'No search query provided',
                            'status': '1', 'status_code': f'{400}'})
        # Perform search based on the query using MongoDB
        employees = collection.find({'empRole': {'$regex': f'{search_query}', '$options': 'i'}})
        search_results = []
        if employees:
            for employee in employees:
                search_results.append({
                    '_id': str(employee['_id']),
                    'empId': employee['empId'],
                    'empName': employee['empName'],
                    'empRole': employee['empRole'],
                    'empSalary': employee['empSalary']
                })
        return jsonify(search_results)


    @staticmethod
    def dynamic_search_text(collection, search_query, field_name):
        if not search_query:
            return jsonify({'message': 'No search query provided',
                            'status': '1', 'status_code': f'{400}'})
        employees = collection.find({f'{field_name}': {'$regex': f'{search_query}', '$options': 'i'}})
        search_results = []
        if employees:
            for employee in employees:
                search_results.append({
                    '_id': str(employee['_id']),
                    'empId': employee['empId'],
                    'empName': employee['empName'],
                    'empRole': employee['empRole'],
                    'empSalary': employee['empSalary']
                })
        return jsonify(search_results)




