from flask_web.Databases.User import User
from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth
import json
from flask_web import db, app
import time
import datetime
userModule = Blueprint('userModule',__name__)

@userModule.route('/', methods=['GET'])
# @auth.login_required
def getAllUsers():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    blurry = request.args.get("blurry")
    if blurry is not  None:
        totalElements = User.query.filter(User.username.like("%" + blurry + "%")).count()
        users = User.query.filter(User.username.like("%" + blurry + "%")).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = User.query.count()
        users = User.query.offset((page - 1) * size).limit(size).all()
    # users = User.query.all()
    return_data = {}
    data = []
    for u in users:
        data.append(u.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements
    return jsonify({'code':'200','data':return_data,'error':''})


@userModule.route('/getUserInfo/<loginname>',methods=['GET'])
@auth.login_required
def getUserInfo(loginname):
    user = User.query.filter_by(loginname = loginname).first()
    return jsonify({'code':'200','data':user.to_json()})


@userModule.route('/editPassword',methods = ['PUT'])
@auth.login_required
def editPassword():
    data = json.loads(str(request.data, encoding="utf-8"))
    user = User.query.filter_by(loginname = g.user.loginname).first()
    if user and user.verify_password(data['oldPass']) :
        user.hash_password(data['confirmPass'])
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'修改密码失败'})
        return jsonify({'code': 200, 'msg': "修改密码成功"})
    else:
        return jsonify({'code': 500, 'msg': "请检查输入"})



@userModule.route('/addUserInfo',methods = ['PUT'])
@auth.login_required
def addUserInfo():
    data = json.loads(str(request.data, encoding = "utf-8"))
    user = User.query.filter_by(loginname = g.user.loginname).first()
    try:
        user.username = data['username']
        user.telphone = data['telphone']
        user.userdetail = data['userdetail']
        user.company = data['company']
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新个人信息失败'})
    return jsonify({'code':'200','data':'','msg':'更新个人信息成功'})


@userModule.route('/addUser',methods=['POST'])
@auth.login_required
def addUser():
    data = json.loads(str(request.data, encoding = "utf-8"))
    userName = data['userName']
    userPsw = data['userPassword']
    userDetail = data['userDetail']
    lastlogin = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = User.query.filter_by(loginname = userName).first()
    # 用户名唯一
    if user is None:
        u = User(userName, userPsw, userDetail, lastlogin)
        u.hash_password(userPsw)
        try:
            db.session.add(u)
            db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
        except Exception as e:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'添加失败'})
        return jsonify({'status':'success','data':'','msg':'添加成功'})
    else:
        return jsonify({'status':'error','data':'','error':'添加失败'})

@userModule.route('/resetPassword', methods = ['PUT'])
@auth.login_required
def resetPassword():
    data = json.loads(str(request.data, encoding = "utf-8"))
    user = User.query.filter_by(id = int(data['id'])).first()
    print(user.to_json())
    try:
        user.hash_password(app.config['DEFAULT_PASSWORD'])
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'重置密码失败'})
    return jsonify({'status':'success','data':'','msg':'重置密码成功'}) 



@userModule.route('/deleteUser/<int:id>', methods = ['DELETE'])
@auth.login_required
def delUser(id):
    user = User.query.filter_by(id = id).first()
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})



@userModule.route('/batchresetPassword', methods = ['POST'])
@auth.login_required
def batch_reset_password():
    data = json.loads(str(request.data, encoding = "utf-8"))
    ids = data['ids'].split(",")
    for i in ids:
        user = User.query.filter_by(id = int(i)).first()
        try:
            user.hash_password(app.config['DEFAULT_PASSWORD'])
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'重置密码失败'})
    return jsonify({'status':'success','data':'','msg':'重置密码成功'}) 


@userModule.route('/deleteBatchuser', methods = ['POST'])
@auth.login_required
def batch_delete_password():
    data = json.loads(str(request.data, encoding = "utf-8"))
    ids = data['ids'].split(",")
    for i in ids:
        user = User.query.filter_by(id = int(i)).first()
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})