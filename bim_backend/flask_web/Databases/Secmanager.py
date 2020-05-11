from flask_web import db, app, redis
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from passlib.apps import custom_app_context

class Secmanager(db.Model):
    _tablename_ = "secmanager"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    device_name = db.Column(db.String(20))
    specification = db.Column(db.String(20))
    number = db.Column(db.Integer)
    project = db.relationship('Project')
    def __init__(self, project_id, device_name, specification, number):
        super(Secmanager, self).__init__()
        self.project_id = project_id
        self.device_name = device_name
        self.specification = specification
        self.number = number
    def to_json(self):
        json_data = {
            'id': self.id,
            'project_id': self.project_id,
            'device_name': self.device_name,
            'specification': self.specification,
            'number': self.number,
            'project': self.project.to_json()
        }
        return json_data