from flask_web.Databases.ImagePath import ImagePath
from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string

structureModule = Blueprint('structureModule',__name__)


def changeToTreeItem(data):
    item = {"id": data['id'], "label": data['imageName'], "path": data['imageUrl'],"imageUpVideo": data['id'],"imageButtonVideo":""}
    return item

@structureModule.route('/tree',methods = ['GET'])
def getTree():
    belong = request.args.get("belong")
    imageInfos = ImagePath.query.filter(ImagePath.belong.like("%" + belong + "%"))
    data = {"id": 0, "label": belong, "children": []}
    for img in imageInfos:
        temp = img.to_json()
        data['children'].append(changeToTreeItem(temp))
    return jsonify({'status': 'success', 'data': data, 'msg': ''})