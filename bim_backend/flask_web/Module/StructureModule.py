from flask_web.Databases.ImagePath import ImagePath
from flask import Blueprint,render_template,request,jsonify,g
from flask_web import auth, app
import json
from flask_web import db
import os,random,string

structureModule = Blueprint('structureModule',__name__)

# : None, 'belong_id': None, 'abstract': ''}
# {'id': 28, 'pid': 0, 'belong': '健康监测系统预留件', 'imageName': '元洪航道桥预
# 留件M7布置图', 'imageUrl': '/健康监测系统预留件/OwdqMTreo4ak3ZPyD9BY8pXG.png', '
# videoUpUrl': None, 'videoLeftUrl': None, 'videoRightUrl': None, 'videoBottomUrl'
# : None, 'belong_id': None, 'abstract': ''}
def changeToTreeItem(data):
    print(data)
    item = {"id": data['id'], "pid": data["pid"], "label": data['imageName'], "imageName": data['imageName'], "path": data['imageUrl'],
            "abstract": data['abstract'], "videoUpUrl": data['videoUpUrl'], "videoLeftUrl": data['videoLeftUrl'], "videoRightUrl": data['videoRightUrl'], "videoBottomUrl":data['videoBottomUrl']}
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
        if (item['pid'] == 0):
            trees.append(item)
            for it in infos:
                if(item['id'] == it['pid']):
                    if("children" not in item):
                        item["children"] = []
                    item["children"].append(it)

    return jsonify({'status': 'success', 'data': trees, 'msg': ''})