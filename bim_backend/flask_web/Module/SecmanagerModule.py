from flask_web.Databases.Secmanager import Secmanager
from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string

secmanagerModule = Blueprint('secmanagerModule',__name__)

@secmanagerModule.route('/', methods=['GET'])
@auth.login_required
def getAll():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    blurry = request.args.get("blurry")
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

@secmanagerModule.route('/test',methods = ['POST'])
# @auth.login_required
def test():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 24))
    file = request.files['file']
    filename = file.filename
    # 将图片名转化成24位随机码 以防重复
    imgName = ran_str + os.path.splitext(filename)[-1]
    save_path = os.path.join(app.config["BASE_DIR"], imgName)

    file.save(save_path)
    return jsonify({'status': 'success', 'data': '', 'msg': '文件添加成功'})










