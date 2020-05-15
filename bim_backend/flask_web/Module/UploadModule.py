from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string
from flask_web.Databases.ImagePath import ImagePath, StructorInfo




base = app.config["BASE_DIR"]
uploadModule = Blueprint('uploadModule',__name__)


@uploadModule.route('/img',methods = ['POST'])
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
    return jsonify({'status':'success','data':'','msg':'添加成功'})

