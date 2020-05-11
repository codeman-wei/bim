from flask_web import db

class Project(db.Model):
    """docstring for ClassName"""
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(255), nullable=True)
    item_img_href = db.Column(db.String(255), nullable=True)

    def __init__(self, item_name, item_img_href):
        self.item_name = item_name
        self.item_img_href = item_img_href

    def to_json(self):
        json_data = {
            'id' : self.id,
            'item_name': self.item_name,
            'item_img_href': self.item_img_href,
        }
        return json_data



class SubProject(db.Model):
    """docstring for SubProject"""
    __tablename__ = 'sub_project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=True)
    sub_project_name = db.Column(db.String(255), nullable=True)
    sub_project_status = db.Column(db.String(255), nullable=True)
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
    __tablename__ = 'participants_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=True)
    participants_name = db.Column(db.String(255), nullable=True)
    participants_sex = db.Column(db.Integer, nullable=True)
    participants_tel = db.Column(db.String(255))   
    participants_work_status = db.Column(db.Integer, nullable = True)   
    participants_qualification = db.Column(db.String(255))   
    def __init__(self, project_id, participants_name, 
        participants_sex, participants_tel, participants_work_status, participants_qualification):
        self.project_id = project_id
        self.participants_name = participants_name,
        self.participants_sex = participants_sex,
        self.participants_tel = participants_tel,
        self.participants_work_status = participants_work_status,
        self.participants_qualification = participants_qualification
    def to_json(self):
        json_data = {
            'id': self.id,
            'project_id': self.project_id,
            'participants_name': self.participants_name,
            'participants_sex': self.participants_sex,
            'participants_tel': self.participants_tel,
            'participants_work_status': self.participants_work_status,
            'participants_qualification': self.participants_qualification
        }
        return json_data
    



        