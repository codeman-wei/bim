from flask_web.Databases.Secmanager import Secmanager
from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string

secmanagerModule = Blueprint('secmanagerModule',__name__)

@secmanagerModule.route('/', methods=['GET'])
# @auth.login_required
def getAll():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    blurry = request.args.get("blurry")
    # blurry = None
    if blurry is not None:
        totalElements = Secmanager.query.filter(Secmanager.device_name.like("%" + blurry + "%")).count()
        items = Secmanager.query.filter(Secmanager.device_name.like("%" + blurry + "%")).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = Secmanager.query.count()
        items = Secmanager.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for item in items:
        data.append(item.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements
    return jsonify({'code': '200', 'data': return_data, 'error': ''})

@secmanagerModule.route('/add', methods = ['POST'])
# @auth.login_required
def add():
    data = json.loads(str(request.data, encoding = "utf-8"))
    sec = Secmanager(
        project_id=data["project_id"],
        device_name=data['device_name'],
        specification=data['specification'],
        number=data['number'],
    )
    try:
        db.session.add(sec)
        db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'添加失败'})
    return jsonify({'status':'success','data':'','msg':'添加成功'})


basedir = os.path.abspath(os.path.dirname(__file__))
@secmanagerModule.route('/edit', methods = ['PUT'])
# @auth.login_required
def edit():
    data = json.loads(str(request.data, encoding="utf-8"))
    sec = Secmanager.query.filter_by(id=data['id']).first()
    sec.project_id = data['project_id'],
    sec.device_name = data['device_name'],
    sec.specification = data['specification'],
    sec.number = data['number'],
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    return jsonify({'status':'success','data':'','msg':'更新成功'})


@secmanagerModule.route('/del/<int:id>',methods = ['DELETE'])
# @auth.login_required
def delete(id):
    sec = Secmanager.query.filter_by(id=id).first()
    try:
        db.session.delete(sec)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'data':'', 'error': '删除失败'})
    return jsonify({'status': 'success', 'data': '', 'msg': '删除成功'})


@secmanagerModule.route('/delAll',methods = ['DELETE'])
# @auth.login_required
def deleteAll():
    data = json.loads(str(request.data, encoding="utf-8"))
    ids = data['ids']
    for i in ids:
        sec = Secmanager.query.filter_by(id=i).first()
        try:
            db.session.delete(sec)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'error', 'data': '', 'error': '删除失败'})
    return jsonify({'status': 'success', 'data': '', 'msg': '删除成功'})












