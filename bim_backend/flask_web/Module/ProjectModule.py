from flask_web.Databases.Project import Project, SubProject, ParticipantsInfo
from flask import Blueprint,render_template, request, jsonify
from flask_web import auth, db, app
import json
import os, random, string
from datetime import datetime

# 在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global
projectModule = Blueprint('projectModule',__name__)
base = app.config["BASE_DIR"]

@projectModule.route('/',methods = ['GET'])
@auth.login_required
def getAllProject():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    image_name = request.args.get("imageName")
    if image_name is not None:
        totalElements = Project.query.filter(Project.item_name.like("%" + image_name + "%")).count()
        projects = Project.query.filter(Project.item_name.like("%" + image_name + "%")).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = Project.query.count()
        projects = Project.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for index in range(0, len(projects), 4):
        temp = []
        for p in projects[index: index + 4]:
            temp.append(p.to_json())
        data.append(temp)
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'code':'200','data':return_data,'error':''})



@projectModule.route('/addProject',methods = ['POST'])
@auth.login_required
def addProject():
    data = request.form
    item_name = data.get("item_name")
    item_status = data.get("item_status")
    file = request.files['file']
    tempDir = os.path.join(base, 'image')
    tempDir = os.path.join(tempDir, "projectImg")
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 24))
    imgName = ran_str + os.path.splitext(file.filename)[-1]
    save_path = os.path.join(tempDir, imgName)
    file.save(save_path)
    imageUrl = '/projectImg/' + imgName
    p = Project(item_name = item_name, item_status = item_status, item_img_href = imageUrl)
    try:
        db.session.add(p)
        db.session.commit()  # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'data': '', 'error': '添加失败'})
    return jsonify({'status': 'success', 'data': '', 'msg': '添加成功'})

@projectModule.route('/editProject',methods = ['PUT'])
@auth.login_required
def editProject():
    data = request.form
    id = data.get("id")
    item_name = data.get("item_name")
    item_status = data.get("item_status")
    pinfo = Project.query.filter_by(id = data['id']).first()
    try:
        file = request.files['file']
        tempDir = os.path.join(base, 'image')
        tempDir = os.path.join(tempDir, "projectImg")
        if not os.path.exists(tempDir):
            os.mkdir(tempDir)
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 24))
        imgName = ran_str + os.path.splitext(file.filename)[-1]
        save_path = os.path.join(tempDir, imgName)
        file.save(save_path)
        imageUrl = '/projectImg/' + imgName
        pinfo.item_img_href = imageUrl
    except Exception as e:
        pass
    pinfo.item_name = item_name
    pinfo.item_status = int(item_status)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    # 将编辑好的信息返回前端 方便页面更新
    return jsonify({'status': 'success', 'data':'', 'msg': '更新成功'})


@projectModule.route('/getProjectScheduleInfo', methods = ['GET'])
@auth.login_required
def getProjectScheduleInfo():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    totalElements = Project.query.count()
    projects = Project.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for p in projects:
        data.append(p.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'status':'success','data':return_data,'msg':'请求数据成功'})



@projectModule.route('/subproject',methods = ['GET'])
@auth.login_required
def getSubprojectById():
    print(request.args)
    pid = int(request.args.get("projectid"))
    sub_project_name = request.args.get("sub_project_name")
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    subs = []
    # 默认按照开始时间排序
    if sub_project_name is not None:
        totalElements = SubProject.query.filter_by(project_id = pid).filter(SubProject.sub_project_name.like("%" + sub_project_name + "%")).count()
        subs = SubProject.query.filter_by(project_id = pid).filter(SubProject.sub_project_name.like("%" + sub_project_name + "%")).order_by(SubProject.start_time).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = SubProject.query.filter_by(project_id = pid).count()
        subs = SubProject.query.filter_by(project_id = pid).order_by(SubProject.start_time).offset((page - 1) * size).limit(size).all()
    data = []
    return_data = {}
    for sp in subs:
        data.append(sp.to_json())
    return_data['totalElements'] = totalElements
    return_data['content'] = data
    return jsonify({'code':'200','data':return_data,'error':''})

@projectModule.route('/addsubproject', methods = ['POST'])
@auth.login_required
def addsubproject():
    data = json.loads(str(request.data, encoding = "utf-8"))
    sup = SubProject(
            project_id = data['project_id'],
            sub_project_name = data['sub_project_name'],
            start_time = data['start_time'],
            end_time = data['end_time'],
            sub_project_status = data['sub_project_status'],
        )
    try:
        db.session.add(sup)
        db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'添加失败'})
    return jsonify({'status':'success','data':'','msg':'添加成功'})


@projectModule.route('/editsubproject', methods = ['PUT'])
@auth.login_required
def editsubproject():
    data = json.loads(str(request.data, encoding = "utf-8"))
    print(data)
    sub = SubProject.query.filter_by(id = data['id']).first()
    sub.project_id = data['project_id']
    sub.sub_project_name = data['sub_project_name']
    sub.start_time = data['start_time']
    sub.end_time = data['end_time']
    sub.sub_project_status = data['sub_project_status']
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    return jsonify({'status':'success','data':'','msg':'更新成功'})


@projectModule.route('/delsubproject/<int:id>', methods = ['DELETE'])
@auth.login_required
def delsubproject(id):
    sub = SubProject.query.filter_by(id = id).first()
    try:
        db.session.delete(sub)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})

@projectModule.route('/delbatchproject', methods = ['POST'])
@auth.login_required
def delbatchproject():
    data = json.loads(str(request.data, encoding = "utf-8"))
    ids = data['ids'].split(",")
    for i in ids:
        sub = SubProject.query.filter_by(id = i).first()
        try:
            db.session.delete(sub)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})





@projectModule.route('/list',methods = ['GET'])
@auth.login_required
def getProjectList():
    items = Project.query.all()
    data = []
    for item in items:
        data.append(item.to_json())
    return jsonify({'code':'200','data':data,'error':''})




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
