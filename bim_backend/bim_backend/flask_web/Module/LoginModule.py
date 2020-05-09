from flask import Blueprint,render_template,request,jsonify
from flask_web import auth, app, redis
from flask_web.Databases.User import User
from flask import g
from flask import make_response
import re

# 在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global
loginModule = Blueprint('loginModule',__name__)
 

@auth.verify_password
def verify_password(name_or_token, password):
    if not name_or_token:
        return False
    name_or_token = re.sub(r'^"|"$', '', name_or_token)
    u = User.verify_auth_token(name_or_token)
    if not u:
        u = User.query.filter_by(loginname = name_or_token).first()
        if not u or not u.verify_password(password):
            return False
    g.user = u
    return True



@loginModule.route("/login",methods=['GET','POST'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    # redis.set(g.user.id,token)
    # redis.expire(g.user.id, app.config['Expiration']*2)  
    return jsonify({'code': 200, 'msg': "登录成功", 'token': token.decode('ascii'), 'name': g.user.loginname})



@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 200)

 
