from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string
from flask_web.Databases.ImagePath import ImagePath, StructorInfo




base = app.config["BASE_DIR"]
uploadModule = Blueprint('uploadModule',__name__)

def randomName(file, len=24):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, len))
    suffix = os.path.splitext(file.filename)[-1]
    return ran_str + suffix

@uploadModule.route('/uploadImg',methods = ['POST'])
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
    imgInfo = ImagePath(belong=belong, pid=0, image_name=imageName, image_url = imageUrl, abstract = imgaeAbstract)
    try:
        db.session.add(imgInfo)
        db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'添加失败'})
    return jsonify({'status':'success','data': '','msg':'添加成功'})


@uploadModule.route('/editImg',methods = ['PUT'])
@auth.login_required
def editImg():
    data = request.form
    id = data.get('id')
    imageName = data.get("imageName")
    imgaeAbstract = data.get("imgaeAbstract")
    belong = data.get("structName")
    imgInfo = ImagePath.query.filter_by(id = data['id']).first()
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
    # try:
    #     db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({'status':'error','data':'','error':'更新失败'})
    return jsonify({'status':'success','data': imgInfo.to_json(),'msg':'更新成功'})

@uploadModule.route('/video',methods = ['POST'])
# @auth.login_required
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
        pass
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'上传失败'})
    return jsonify({'status': '200', 'data': '', 'msg': '更新成功'})

