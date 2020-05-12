from flask_web import db


class ImagePath(db.Model):
    """docstring for ImagePath"""
    __tablename__ = 'image_path'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    belong = db.Column(db.String(255))
    image_name = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    vedio_up_url = db.Column(db.String(255))
    vedio_left_url = db.Column(db.String(255))
    vedio_right_url = db.Column(db.String(255))
    vedio_bottom_url = db.Column(db.String(255))

    def __init__(self, belong, image_name, image_url, vedio_up_url, vedio_left_url, vedio_right_url, vedio_bottom_url):
        super(ImagePath, self).__init__()
        self.belong = belong
        self.image_name = image_name
        self.image_url = image_url
        self.vedio_up_url = vedio_up_url
        self.vedio_left_url = vedio_left_url
        self.vedio_right_url = vedio_right_url
        self.vedio_bottom_url = vedio_bottom_url
    def to_json(self):
        json_data = {
            'id' : self.id,
            'belong': self.belong,
            'imageName': self.image_name,
            'imageUrl': self.image_url,
            'videoUpUrl': self.vedio_up_url,
            'videoLeftUrl': self.vedio_left_url,
            'videoRightUrl': self.vedio_right_url,
            'videoBottomUrl': self.vedio_bottom_url,
        }
        return json_data