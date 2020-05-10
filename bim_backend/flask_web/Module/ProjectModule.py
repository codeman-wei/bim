from flask_web.Databases.Project import Project, SubProject, ParticipantsInfo
from flask import Blueprint,render_template, request, jsonify
from flask_web import auth, db
import json

# 在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global
projectModule = Blueprint('projectModule',__name__)


@projectModule.route('/',methods = ['GET'])
@auth.login_required
def getAllEmp():
    projects = Project.query.all()
    return_data = []
    for index in range(0, len(projects), 3):
        temp = []
        for p in projects[index: index + 3]:
            temp.append(p.to_json())
        return_data.append(temp)
    return jsonify({'code':'200','data':return_data,'error':''})

@projectModule.route('/subproject',methods = ['GET'])
@auth.login_required
def getSubprojectById():
    print(request.args)
    pid = int(request.args.get("id"))
    subp = SubProject.query.filter_by(project_id = pid).all()
    return_data = []
    for sp in subp:
        return_data.append(sp.to_json())
    return jsonify({'code':'200','data':return_data,'error':''})


@projectModule.route('/participantsinfo', methods = ['GET'])
@auth.login_required
def getParticipantsInfo():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    totalElements = Project.query.count()
    projects = Project.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for p in projects:
        item_total = ParticipantsInfo.query.filter_by(project_id = p.id).count()
        pdata = {
            'id': p.id,
            'item_total': item_total,
            'item_name': p.item_name
        }
        data.append(pdata)
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'status':'success','data':return_data,'msg':'请求数据成功'})


@projectModule.route('/participantsinfobypid', methods = ['GET'])
@auth.login_required
def getParticipantsInfoByPID():
    pid = int(request.args.get("projectid")) #page=1&size=10&projectid=1&sort=id,desc 
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    participants_name = request.args.get("participants_name")
    if participants_name is not None:
        totalElements = ParticipantsInfo.query.filter_by(project_id = pid).filter(ParticipantsInfo.participants_name.like("%" + participants_name + "%")).count()
        pinfos = ParticipantsInfo.query.filter_by(project_id = pid).filter(ParticipantsInfo.participants_name.like("%" + participants_name + "%")).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = ParticipantsInfo.query.filter_by(project_id = pid).count()
        pinfos = ParticipantsInfo.query.filter_by(project_id = pid).offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for p in pinfos:
        data.append(p.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'status':'success','data':return_data,'msg':'请求数据成功'})


@projectModule.route('/addparticipantsinfo', methods = ['POST'])
@auth.login_required
def addParticipantsinfo():
    data = json.loads(str(request.data, encoding = "utf-8"))
    pinfo = ParticipantsInfo(
            project_id = data['project_id'],
            participants_name = data['participants_name'],
            participants_sex = data['participants_sex'],
            participants_tel = data['participants_tel'],
            participants_work_status = data['participants_work_status'],
            participants_qualification = data['participants_qualification']
        )
    try:
        db.session.add(pinfo)
        db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'添加失败'})
    return jsonify({'status':'success','data':'','msg':'添加成功'})


@projectModule.route('/editparticipantsinfo', methods = ['PUT'])
@auth.login_required
def editParticipantsinfo():
    data = json.loads(str(request.data, encoding = "utf-8"))
    pinfo = ParticipantsInfo.query.filter_by(id = data['id']).first()
    pinfo.project_id = data['project_id'],
    pinfo.participants_name = data['participants_name'],
    pinfo.participants_sex = data['participants_sex'],
    pinfo.participants_tel = data['participants_tel'],
    pinfo.participants_work_status = data['participants_work_status'],
    pinfo.participants_qualification = data['participants_qualification']
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    return jsonify({'status':'success','data':'','msg':'更新成功'})

@projectModule.route('/deleteparticipantsinfo/<int:id>', methods = ['DELETE'])
@auth.login_required
def deleteParticipantsinfo(id):
    pinfo = ParticipantsInfo.query.filter_by(id = id).first()
    try:
        db.session.delete(pinfo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})


@projectModule.route('/deletebatchparticipantsinfo', methods = ['POST'])
@auth.login_required
def deleteBatchParticipantsinfo():
    data = json.loads(str(request.data, encoding = "utf-8"))
    ids = data['ids'].split(",")
    for i in ids:
        pinfo = ParticipantsInfo.query.filter_by(id = i).first()
        try:
            db.session.delete(pinfo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})