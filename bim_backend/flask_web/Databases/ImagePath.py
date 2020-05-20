from flask_web import db

class StructorInfo(db.Model):
    """docstring for StructorInfo"""
    __tablename__ = 'struct_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    struct_name = db.Column(db.String(255))
    def __init__(self, struct_name):
        self.struct_name = struct_name
    def to_json(self):
        json_data = {
            'id': self.id,
            'struct_name': self.struct_name
        }
        return json_data

        


class ImagePath(db.Model):
    """docstring for ImagePath"""
    __tablename__ = 'image_path'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pid = db.Column(db.Integer)
    belong = db.Column(db.String(255))
    image_name = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    vedio_up_url = db.Column(db.String(255))
    vedio_left_url = db.Column(db.String(255))
    vedio_right_url = db.Column(db.String(255))
    vedio_bottom_url = db.Column(db.String(255))
    abstract = db.Column(db.String(255))
    belong_id = db.Column(db.Integer)


    def __init__(self, belong = None, pid = None,
        image_name = None, image_url = None, 
        vedio_up_url = None , vedio_left_url= None , vedio_right_url = None, 
        vedio_bottom_url = None, belong_id = None, abstract = None):
        self.belong = belong
        self.pid = pid
        self.image_name = image_name
        self.image_url = image_url
        self.vedio_up_url = vedio_up_url
        self.vedio_left_url = vedio_left_url
        self.vedio_right_url = vedio_right_url
        self.vedio_bottom_url = vedio_bottom_url
        self.belong_id = belong_id
        self.abstract = abstract
    def to_json(self):
        json_data = {
            'id': self.id,
            'pid': self.pid,
            'belong': self.belong,
            'imageName': self.image_name,
            'imageUrl': self.image_url,
            'videoUpUrl': self.vedio_up_url,
            'videoLeftUrl': self.vedio_left_url,
            'videoRightUrl': self.vedio_right_url,
            'videoBottomUrl': self.vedio_bottom_url,
            'belong_id': self.belong_id,
            'abstract': self.abstract
        }
        return json_data


class UpdataLog(db.Model):
    __tablename__ = 'update_image_log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updatetime = db.Column(db.DateTime)
    loginname = db.Column(db.String(255), nullable = True)
    belong = db.Column(db.String(255), nullable = True)
    reason = db.Column(db.String(255), nullable = True)
    op = db.Column(db.Integer, nullable = True)
    def __init__(self, updatetime , loginname , belong , reason , op ):
        self.updatetime = updatetime
        self.loginname = loginname
        self.belong = belong
        self.reason = reason
        self.op = op

    def to_json(self):
        json_data = {
            'id': self.id,
            'updatetime': self.updatetime,
            'belong': self.belong,
            'reason': self.reason,
            'loginname': self.loginname,
            'op' : self.op
        }
        return json_data
