from flask_web import db



class Employee(db.Model):
    """docstring for Employee"""
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_name = db.Column(db.String(255), nullable=True)
    employee_number = db.Column(db.String(255), nullable=True)
    employee_tel = db.Column(db.String(255))
    employee_id_number = db.Column(db.String(255))
    employee_dept = db.Column(db.String(255))
    employee_job = db.Column(db.String(255))
    employee_project = db.Column(db.String(255))
    def __init__(self, employee_name, employee_number, employee_tel, employee_id_number, employee_dept, employee_job, employee_project):
        super(Employee, self).__init__()
        self.employee_name = employee_name
        self.employee_number = employee_number
        self.employee_tel = employee_tel
        self.employee_id_number = employee_id_number
        self.employee_dept = employee_dept
        self.employee_job = employee_job
        self.employee_project = employee_project
    def to_json(self):
        json_data = {
            'id' : self.id,
            'employee_name': self.employee_name,
            'employee_number': self.employee_number,
            'employee_tel': self.employee_tel,
            'employee_id_number': self.employee_id_number,
            'employee_dept': self.employee_dept,
            'employee_job': self.employee_job,
            'employee_project' :self.employee_project
        }
        return json_data