from flask_web import db

class Project(db.Model):
    """docstring for ClassName"""
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(255), nullable=True)
    item_img_href = db.Column(db.String(255), nullable=True)
    item_status = db.Column(db.Integer, nullable = True)
    def __init__(self, item_name, item_img_href, item_status):
        self.item_name = item_name
        self.item_img_href = item_img_href
        self.item_status = item_status
    def to_json(self):
        json_data = {
            'id' : self.id,
            'item_name': self.item_name,
            'item_img_href': self.item_img_href,
            'item_status': self.item_status
        }
        return json_data



class SubProject(db.Model):
    """docstring for SubProject"""
    __tablename__ = 'sub_project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=True)
    sub_project_name = db.Column(db.String(255), nullable=True)
    sub_project_status = db.Column(db.Integer, nullable = True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, project_id, sub_project_name, sub_project_status, start_time, end_time):
        self.project_id = project_id
        self.sub_project_name = sub_project_name
        self.sub_project_status = sub_project_status
        self.start_time = start_time
        self.end_time = end_time
    def to_json(self):
        json_data = {
            'id': self.id,
            'project_id': self.project_id,
            'sub_project_name': self.sub_project_name,
            'sub_project_status': self.sub_project_status,
            'start_time': self.start_time,
            'end_time': self.end_time,
        }
        return json_data


class ParticipantsInfo(db.Model):
    """docstring for participantsInfo"""
    __tablename__ = 'participants_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=True)
    participants_name = db.Column(db.String(255), nullable=True)
    participants_tel = db.Column(db.String(255))   
    participants_work_status = db.Column(db.Integer, nullable = True)   
    participants_duty = db.Column(db.Text(200))   
    participants_dept = db.Column(db.String(255))
    participants_position = db.Column(db.String(255))
    participants_number = db.Column(db.String(255))
    def __init__(self, project_id, participants_name, 
        participants_tel, participants_work_status, participants_duty, participants_dept, participants_position, participants_number):
        self.project_id = project_id
        self.participants_name = participants_name
        self.participants_tel = participants_tel
        self.participants_work_status = participants_work_status
        self.participants_duty = participants_duty
        self.participants_dept = participants_dept
        self.participants_position = participants_position
        self.participants_number = participants_number
    def to_json(self):
        json_data = {
            'id': self.id,
            'project_id': self.project_id,
            'participants_name': self.participants_name,
            'participants_tel': self.participants_tel,
            'participants_work_status': self.participants_work_status,
            'participants_duty': self.participants_duty,
            'participants_dept': self.participants_dept,
            'participants_position': self.participants_position,
            'participants_number': self.participants_number
        }
        return json_data



        