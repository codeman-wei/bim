from flask import Flask,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from redis import StrictRedis
import os


redis = StrictRedis(host='localhost', port=6379, db=0)
auth = HTTPBasicAuth()



app = Flask(__name__)

# STATIC_PATH = r"D:\code\temp\static"
# app = Flask(__name__,static_folder=STATIC_PATH)

CORS(app, supports_credentials=True)

app.config['BASE_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
app.config['SECRET_KEY'] = '123456'
app.config['DEFAULT_PASSWORD'] = '123456'
app.config['Expiration'] = 600
# 指定数据库的链接信息
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/bim_db"
# 这个配置将来会被禁用,设置为True或者False可以解除警告信息,建议设置False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SQLALCHEMY_RECORD_QUERIES'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


# 注册蓝图

from flask_web.Module import LoginModule, UserModule, EmployeeModule, ProjectModule,SecmanagerModule

app.register_blueprint(LoginModule.loginModule)
app.register_blueprint(UserModule.userModule, url_prefix="/user")
app.register_blueprint(EmployeeModule.employeeModule, url_prefix="/employee")
app.register_blueprint(ProjectModule.projectModule, url_prefix="/project")
app.register_blueprint(SecmanagerModule.secmanagerModule, url_prefix="/secmanager")