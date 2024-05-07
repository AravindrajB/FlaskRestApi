from flask import Blueprint, request
from Project.app.services.employee_service import EmployeeService
from Project.app.config import Config


employee_bp = Blueprint('employee_bp', __name__)

# collection will be used to all method, so we declared here
collection = Config.collection


# POST METHOD - ADD EMPLOYEE
@employee_bp.route('/addEmployee', methods=['POST'])
def add_employee():
    data = request.get_json()  # we can use -> request.json this is also works
    # empId = data.get('empId')
    # empName = data.get('empName')
    # empSalary = data.get('empSalary')
    # empRole = data.get('empRole')
    # client = MongoClient(Config.MONGO_URI)
    # db = client['Promantus']
    # collection = db["FlaskRestApi"]
    # collection = Config.collection
    result = EmployeeService.add_employee(data, collection)
    return result


# GET METHOD - GET ALL EMPLOYEE
@employee_bp.route('/getEmployees', methods=['GET'])
def get_employees():
    result = EmployeeService.get_employees(collection)
    return result


# GET PARTICULAR EMPLOYEE
@employee_bp.route('/getEmployee/<Id>', methods=['GET'])
def get_employee(Id):
    employee = EmployeeService.get_employee(collection, Id)
    return employee


# PUT - UPDATE EMPLOYEE
@employee_bp.route('/updateEmployee/<Id>', methods=['PUT'])
def update_employee(Id):
    data = request.get_json()
    result = EmployeeService.update_employee(data, collection, Id)
    return result


@employee_bp.route('/removeEmployee/<Id>', methods=['DELETE'])
def remove_employee(Id):
    result = EmployeeService.remove_employee(collection, Id)
    return result

@employee_bp.route('/search', methods=['GET'])
def search_text():
    # Parse query parameters from the request
    search_query = request.args.get('query')
    # print(search_query)
    result = EmployeeService.search_text(collection, search_query)
    return result

@employee_bp.route('/dynamicsearch/<field_name>', methods=['GET'])
def dynamic_search_text(field_name):
    search_query = request.args.get('query')
    result = EmployeeService.dynamic_search_text(collection, search_query, field_name)
    return result
