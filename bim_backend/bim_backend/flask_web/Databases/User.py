from flask_web import db, app, redis
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from passlib.apps import custom_app_context
import json
import datetime
from flask import g


class User(db.Model):
    """docstring for ClassName"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    loginname = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    telphone = db.Column(db.String(255))
    userdetail = db.Column(db.String(255))
    lastlogin = db.Column(db.DateTime)
    company = db.Column(db.String(255))

    def __init__(self, loginname, password, userdetail, lastlogin):
        super(User, self).__init__()
        self.loginname = loginname
        self.password = password
        self.userdetail = userdetail
        self.lastlogin = lastlogin
        # self.company = company
        # self.telphone = telphone
    # 密码加密
    def hash_password(self, password):
        self.password = custom_app_context.encrypt(password)
    # 密码解析
    def verify_password(self, password):
        return custom_app_context.verify(password, self.password)
    
    # 获取token，有效时间10min
    def generate_auth_token(self, expiration = 60 * 60 * 24 * 15):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({'id': self.id})
    # 解析token，确认登录的用户身份
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            #print(data)
        except SignatureExpired: # valid token, but expired
            print("valid token, but expired")
            return None
            # tokenRedis = redis.get(g.user.id)
            # if tokenRedis is None: # get from redis 
            #     raise AuthFailed(msg='token过期')
            # else:
            #     token = g.user.generate_auth_token()
            #     redis.set(g.user.id, token)
            #     redis.expire(g.user.id, app.config['Expiration']*2)  
            #     return g.user
        except BadSignature:
            return None
            # raise AuthFailed(msg='token不正确')  # invalid token
        user = User.query.get(data['id'])
        return user
    
    def to_json(self):
        json_data = {
            'id' : self.id,
            'username': self.username,
            'loginname': self.loginname,
            'password': self.password,
            'telphone': self.telphone,
            'userdetail': self.userdetail,
            'lastlogin': str(self.lastlogin),
            'company' :self.company
        }
        return json_data


