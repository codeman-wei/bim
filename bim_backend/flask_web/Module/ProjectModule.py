from flask_web.Databases.Project import Project, SubProject
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

@projectModule.route('/list',methods = ['GET'])
# @auth.login_required
def getProjectList():
    items = Project.query.all()
    data = []
    for item in items:
        data.append(item.to_json())
    return jsonify({'code':'200','data':data,'error':''})