from flask_web.Databases.Employee import Employee
from flask import Blueprint,render_template, request, jsonify
from flask_web import auth, db
import json

# 在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global
employeeModule = Blueprint('employeeModule',__name__)

@employeeModule.route('/',methods = ['GET'])
@auth.login_required
def getAllEmp():
    print(request.args)
    page = int(request.args.get("page"))
    size = int(request.args.get("size"))
    employee_name = request.args.get("employee_name")
    print(employee_name)
    if employee_name is not None:
        totalElements = Employee.query.filter(Employee.employee_name.like("%" + employee_name + "%")).count()
        employees = Employee.query.filter(Employee.employee_name.like("%" + employee_name + "%")).offset((page - 1) * size).limit(size).all()
    else:
        totalElements = Employee.query.count()
        employees = Employee.query.offset((page - 1) * size).limit(size).all()
    return_data = {}
    data = []
    for e in employees:
        data.append(e.to_json())
    return_data['content'] = data
    return_data['totalElements'] = totalElements  
    return jsonify({'status':'success','data':return_data,'msg':'请求数据成功'})


@employeeModule.route('/addEmp', methods = ['POST'])
@auth.login_required
def addEmp():
    data = json.loads(str(request.data, encoding = "utf-8"))
    emp = Employee(
            employee_name = data['employee_name'], 
            employee_number = data['employee_number'],
            employee_tel = data['employee_tel'],
            employee_id_number = data['employee_id_number'],
            employee_dept = data['employee_dept'],
            employee_project = data['employee_project'],
            employee_job = data['employee_job']
        )
    try:
        db.session.add(emp)
        db.session.commit()    # flask默认使用事务，所以每一次操作都要提交事务
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'添加失败'})
    return jsonify({'status':'success','data':'','msg':'添加成功'})

@employeeModule.route('/editEmp', methods = ['PUT'])
@auth.login_required
def editEmp():
    data = json.loads(str(request.data, encoding = "utf-8"))
    emp = Employee.query.filter_by(id = data['id']).first()
    emp.employee_name = data['employee_name']
    emp.employee_number = data['employee_number']
    emp.employee_tel = data['employee_tel']
    emp.employee_id_number = data['employee_id_number']
    emp.employee_dept = data['employee_dept']
    emp.employee_project = data['employee_project']
    emp.employee_job = data['employee_job']
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'更新失败'})
    return jsonify({'status':'success','data':'','msg':'更新成功'})

@employeeModule.route('/deleteEmp/<int:id>',methods = ['DELETE'])
@auth.login_required
def delete_emp(id):
    emp = Employee.query.filter_by(id = id).first()
    try:
        db.session.delete(emp)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':'error','data':'','error':'删除失败'})
    return jsonify({'status':'success','data':'','msg':'删除成功'})


@employeeModule.route('/deleteBatchEmp',methods = ['POST'])
@auth.login_required
def delete_batch_emp():
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

