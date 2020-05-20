from flask import Blueprint, render_template, request, jsonify, g
from flask_web import auth, app
import json
from flask_web import db
import os, random, string
from flask_web.Databases.ImagePath import ImagePath, StructorInfo, UpdataLog
from datetime import datetime  
base = app.config["BASE_DIR"]
uploadModule = Blueprint('uploadModule', __name__)


def randomName(file, len=24):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, len))
    suffix = os.path.splitext(file.filename)[-1]
    return ran_str + suffix


@uploadModule.route('/uploadImg', methods=['POST'])
@auth.login_required
def uploadImg():
    data = request.form
    imageName = data.get("imageName")
    imgaeAbstract = data.get("imgaeAbstract")
    belong = data.get("structName")
    file = request.files['file']
    # structorObject = StructorInfo.query.filter_by(struct_name = belong).first()
    # if structorObject is not None:
    #     belong_id = structorObject.to_json().get('id')
    tempDir = os.path.join(base, 'image')
    tempDir = os.path.join(tempDir, belong)
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 24))
    imgName = ran_str + os.path.splitext(file.filename)[-1]
    save_path = os.path.join(tempDir, imgName)
    file.save(save_path)
    imageUrl = '/' + belong + '/' + imgName
    imgInfo = ImagePath(belong=belong, pid=0, image_name=imageName, image_url=imageUrl, abstract=imgaeAbstract)
    try:
        db.session.add(imgInfo)
        db.session.commit()  # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'data': '', 'error': '添加失败'})
    # 添加 updatalog表

    log = UpdataLog(
        loginname = g.user.loginname, 
        belong = belong, 
        reason = "上传" + imageName + "图片", 
        updatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        op = 1)
    try :
        db.session.add(log)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return jsonify({'status': 'success', 'data': '', 'msg': '添加成功'})


@uploadModule.route('/editImg', methods=['PUT'])
@auth.login_required
def editImg():
    data = request.form
    id = data.get('id')
    imageName = data.get("imageName")
    imgaeAbstract = data.get("imgaeAbstract")
    belong = data.get("structName")
    imgInfo = ImagePath.query.filter_by(id=data['id']).first()
    try:
        file = request.files.get('file')
        tempDir = os.path.join(base, 'image')
        tempDir = os.path.join(tempDir, belong)
        if not os.path.exists(tempDir):
            os.mkdir(tempDir)
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 24))
        imgName = ran_str + os.path.splitext(file.filename)[-1]
        save_path = os.path.join(tempDir, imgName)
        file.save(save_path)
        imageUrl = '/' + belong + '/' + imgName
        imgInfo.image_url = imageUrl
    except Exception as e:
        pass
    imgInfo.abstract = imgaeAbstract
    imgInfo.belong = belong
    imgInfo.image_name = imageName
    imgInfo.pid = 0
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    # 将编辑好的信息返回前端 方便页面更新
    log = UpdataLog(
        loginname = g.user.loginname, 
        belong = belong, 
        reason = "更新" + imageName + "图片", 
        updatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        op = 0)   
    try :
        db.session.add(log)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return jsonify({'status': 'success', 'data': changeToItem(imgInfo.to_json()), 'msg': '更新成功'})


@uploadModule.route('/video', methods=['POST'])
@auth.login_required
def uploadVideo():
    file = request.files.get('file')
    belong = request.form.get("belong")
    position = request.form.get("position")
    id = request.form.get("id")

    tempDir = os.path.join(base, 'video')
    tempDir = os.path.join(tempDir, belong)

    info = ImagePath.query.filter_by(id=id).first()
    try:
        if not os.path.exists(tempDir):
            os.mkdir(tempDir)
        fileName = randomName(file)
        save_path = os.path.join(tempDir, fileName)
        file.save(save_path)
        # 根据position 来保存视频url到表中对应字段
        url = '/' + belong + '/' + fileName
        toChanged = 'vedio_' + position + '_url'
        code = 'info.' + toChanged + '=url'
        exec(code)
    except Exception as e:
        return jsonify({'status': 'error', 'data': '', 'error': '上传失败'})
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'data': '', 'error': '上传失败'})
    return jsonify({'status': '200', 'data': changeToItem(info.to_json()), 'msg': '更新成功'})


@uploadModule.route('/file', methods=['POST'])
@auth.login_required
def uploadFile():
    print(request.files)
    for key in request.files:
        file = request.files[key]
        tempDir = os.path.join(base, file.filename)
        file.save(tempDir)
    return jsonify({'status': '200', 'data': '', 'msg': '更新成功'})


# 将imagePath对象转化成包含label 和 path 的字典对象
def changeToItem(data):
    item = {"id": data['id'], "pid": data["pid"], "label": data['imageName'], "imageName": data['imageName'], "path": data['imageUrl'],
            "abstract": data['abstract'], "videoUpUrl": data['videoUpUrl'], "videoLeftUrl": data['videoLeftUrl'], "videoRightUrl": data['videoRightUrl'], "videoBottomUrl":data['videoBottomUrl']}
    return item




@uploadModule.route('/updatelist', methods=['GET'])
@auth.login_required
def getupdatelist():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    keyword = request.args.get("keyword")
    if keyword is not None:
        totalElements = UpdataLog.query.filter(UpdataLog.reason.like("%" + keyword + "%")).count()
        logs = UpdataLog.query.filter(UpdataLog.reason.like("%" + keyword + "%")).all()
    else:
        totalElements = UpdataLog.query.count()
        logs = UpdataLog.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for log in logs:
        data.append(log.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'code':'200','data':return_data,'error':''})

