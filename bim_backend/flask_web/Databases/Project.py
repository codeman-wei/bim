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