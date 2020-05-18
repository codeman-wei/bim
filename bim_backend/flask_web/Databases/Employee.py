from flask_web import db


#  该表类似participates_info  记录参与运维工作人员信息
class Employee(db.Model):
    """docstring for Employee"""
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=True)
    emp_name = db.Column(db.String(255), nullable=True)
    emp_tel = db.Column(db.String(255))   
    emp_work_status = db.Column(db.Integer, nullable = True)   
    emp_duty = db.Column(db.Text(200))   
    emp_dept = db.Column(db.String(255))
    emp_position = db.Column(db.String(255))
    emp_number = db.Column(db.String(255))
    def __init__(self, project_id, emp_name, 
        emp_tel, emp_work_status, emp_duty, emp_dept, emp_position, emp_number):
        self.project_id = project_id
        self.emp_name = emp_name
        self.emp_tel = emp_tel
        self.emp_work_status = emp_work_status
        self.emp_duty = emp_duty
        self.emp_dept = emp_dept
        self.emp_position = emp_position
        self.emp_number = emp_number
    def to_json(self):
        json_data = {
            'id': self.id,
            'project_id': self.project_id,
            'emp_name': self.emp_name,
            'emp_tel': self.emp_tel,
            'emp_work_status': self.emp_work_status,
            'emp_duty': self.emp_duty,
            'emp_dept': self.emp_dept,
            'emp_position': self.emp_position,
            'emp_number': self.emp_number
        }
        return json_data