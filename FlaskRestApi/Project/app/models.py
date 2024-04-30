class Employee:

    def __init__(self, empId, empName, empSalary, empRole):
        self.empId = empId
        self.empName = empName
        self.empSalary = empSalary
        self.empRole = empRole

    def to_dict(self):
        return {
            'empId': self.empId,
            'empName': self.empName,
            'empSalary': self.empSalary,
            'empRole': self.empRole
        }

