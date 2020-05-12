from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string


uploadModule = Blueprint('uploadModule',__name__)


@uploadModule.route('/img/<test>',methods = ['POST'])
# @auth.login_required
def uploadImg():
    print()
    # print(json.loads(str(request.data, encoding="utf-8")))
    # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 24))
    # file = request.files['file']
    # filename = file.filename
    # # 将图片名转化成24位随机码 以防重复
    # imgName = ran_str + os.path.splitext(filename)[-1]
    # save_path = os.path.join(app.config["BASE_DIR"], imgName)
    #
    # file.save(save_path)

    # return jsonify({'status': 'success', 'data': imgName, 'msg': '文件添加成功'})
    return jsonify({'status': 'success', 'data': '', 'msg': '文件添加成功'})
