from flask_web.Databases.Employee import Employee
from flask_web.Databases.Project import Project
from flask import Blueprint,render_template, request, jsonify
from flask_web import auth, db
import json

# 在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global
employeeModule = Blueprint('employeeModule',__name__)


@employeeModule.route('/projectInfo', methods = ['GET'])
@auth.login_required
def getProjectInfo():
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    totalElements = Project.query.count()
    projects = Project.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for p in projects:
        item_total = Employee.query.filter_by(project_id = p.id).count()
        pdata = {
            'id': p.id,
            'item_total': item_total,
            'item_name': p.item_name
        }
        data.append(pdata)
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'status':'success','data':return_data,'msg':'请求数据成功'})


@employeeModule.route('/empInfoBypid', methods = ['GET'])
@auth.login_required
def getEmpInfoByPID():
    pid = int(request.args.get("projectid")) #page=1&size=10&projectid=1&sort=id,desc 
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    emp_name = request.args.get("emp_name")
    if emp_name is not None:
        totalElements = Employee.query.filter_by(project_id = pid).filter(Employee.emp_name.like("%" + emp_name + "%")).count()
        emps = Employee.query.filter_by(project_id = pid).filter(Employee.emp_name.like("%" + emp_name + "%")).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = Employee.query.filter_by(project_id = pid).count()
        emps = Employee.query.filter_by(project_id = pid).offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for e in emps:
        data.append(e.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'status':'success','data':return_data,'msg':'请求数据成功'})


@employeeModule.route('/addempinfo', methods = ['POST'])
@auth.login_required
def addEmpInfo():
    data = json.loads(str(request.data, encoding = "utf-8"))

    emp = Employee(
            project_id = data['project_id'],
            emp_name = data['emp_name'],
            emp_number = data['emp_number'],
            emp_tel = data['emp_tel'],
            emp_work_status = data['emp_work_status'],
            emp_dept = data['emp_dept'],
            emp_position = data['emp_position'],
            emp_duty = data['emp_duty']
        )
    try:
        db.session.add(emp)
        db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'添加失败'})
    return jsonify({'status':'success','data':'','msg':'添加成功'})


@employeeModule.route('/editempinfo', methods = ['PUT'])
@auth.login_required
def editEmpInfo():
    data = json.loads(str(request.data, encoding = "utf-8"))
    emp = Employee.query.filter_by(id = data['id']).first()
    emp.project_id = data['project_id'],
    emp.emp_name = data['emp_name'],
    emp.emp_number = data['emp_number'],
    emp.emp_tel = data['emp_tel'],
    emp.emp_work_status = data['emp_work_status'],
    emp.emp_dept = data['emp_dept']
    emp.emp_position = data['emp_position']
    emp.emp_duty = data['emp_duty']
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    return jsonify({'status':'success','data':'','msg':'更新成功'})

@employeeModule.route('/deleteempinfo/<int:id>', methods = ['DELETE'])
@auth.login_required
def deleteEmpInfo(id):
    emp = Employee.query.filter_by(id = id).first()
    try:
        db.session.delete(emp)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})


@employeeModule.route('/deletebatchempinfo', methods = ['POST'])
@auth.login_required
def deleteBatchEmpInfo():
    data = json.loads(str(request.data, encoding = "utf-8"))
    ids = data['ids'].split(",")
    for i in ids:
        emp = Employee.query.filter_by(id = i).first()
        try:
            db.session.delete(emp)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})


