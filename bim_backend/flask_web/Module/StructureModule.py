from flask_web.Databases.ImagePath import ImagePath
from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string

structureModule = Blueprint('structureModule',__name__)


def changeToTreeItem(data):
    item = {"id": data['id'],"belong_id": data["belong_id"], "label": data['imageName'], "imageName": data['imageName'], "path": data['imageUrl']}
    return item

# @structureModule.route('/tree',methods = ['GET'])
# def getTree():
#     belong = request.args.get("belong")
#     imageInfos = ImagePath.query.filter(ImagePath.belong.like("%" + belong + "%"))
#     data = {"id": 0, "label": belong, "children": []}
#     for img in imageInfos:
#         temp = img.to_json()
#         data['children'].append(changeToTreeItem(temp))
#     return jsonify({'status': 'success', 'data': data, 'msg': ''})# @structureModule.route('/tree',methods = ['GET'])

@structureModule.route('/tree',methods = ['GET'])
def getTree():
    belong = request.args.get("belong")
    imageInfos = ImagePath.query.filter_by(belong=belong)
    infos = []
    for img in imageInfos:
        infos.append(changeToTreeItem(img.to_json()))

    trees = []
    for item in infos:
        if (item['belong_id'] == 0):
            trees.append(item)
            for it in infos:
                if(item['id'] == it['belong_id']):
                    if("children" not in item):
                        item["children"] = []
                    item["children"].append(it)

    return jsonify({'status': 'success', 'data': trees, 'msg': ''})