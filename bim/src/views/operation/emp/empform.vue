<template>
    <el-dialog 
        append-to-body 
        :close-on-click-modal="false" 
        :before-close="cancel" 
        :visible.sync= "dialog"
        :title="isAdd ? '新增工作人员信息' : '编辑工作人员信息'"
        width="1000px" 
        @close="cancel">
      <el-form ref="form" :inline="true" :model="form" :rules="rules" size="small" label-width="80px">
        <el-form-item label="员工姓名" prop="employee_name">
            <el-input v-model="form.employee_name" style="width: 145px;" />
        </el-form-item>
        <el-form-item label="员工工号" prop="employee_number">
            <el-input v-model="form.employee_number" style="width: 145px;" />
        </el-form-item>
        <el-form-item label="员工电话" prop="employee_tel">
            <el-input v-model="form.employee_tel" style="width: 145px;" />
        </el-form-item>
        <el-form-item label="岗位证号" prop="employee_id_number">
            <el-input v-model="form.employee_id_number" style="width: 145px;" />
        </el-form-item>
        <el-form-item label="部门" prop="employee_dept">
            <el-input v-model="form.employee_dept" style="width: 145px;" />
        </el-form-item>
        <el-form-item label="所属施工专项" prop="employee_project">
            <el-input v-model="form.employee_project" style="width: 145px;" />
        </el-form-item>
        <el-form-item label="负责内容" prop="employee_job">
            <el-input v-model="form.employee_job" style="width: 145px;" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="resetForm('form')">重置</el-button>
        <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
      </div>
    </el-dialog>
</template>
<script>

import { addEmp, editEmp } from '@/api/operation/employee'
export default {
    props: {
      isAdd: {
        type: Boolean,
        required: true
      }
    },
    data() {
      return {
        title: '',
        dialog: false,
        loading: false,
        form: {
          id: '',
          employee_name: '',
          employee_number: '',
          employee_tel: '',
          employee_id_number: '',
          employee_dept: '',
          employee_project: '',
          employee_job: '',
        },
        rules: {
          employee_name: [
             { required: true, message: '请输入用户名称', trigger: 'blur' },
          
          ]
        },

      }
    },
    methods: {
      cancel() {
          this.resetForm('form')
          this.dialog = false
      },
      doSubmit() {
        this.$refs['form'].validate((valid) => {
          if (valid) {
            this.loading = true
            if (this.isAdd) {
              this.doAdd()
            } 
            else {
              this.doEdit()
            }
          } else {
            return false
          }
        })
      },
      doAdd() {
        addEmp(this.form).then(res => {
          this.dialog = false
          this.resetForm('form')
          this.$notify({
            title: '添加成功',
            type: 'success',
            duration: 2500
          })
          this.loading = false
          this.$parent.initData()
        }).catch(err => {
          this.loading = false
          //console.log(err.response.data.message)
        })
      },
      doEdit() {
        editEmp(this.form).then(res => {
          this.resetForm('form')
          this.$notify({
            title: '修改成功',
            type: 'success',
            duration: 2500
          })
          this.loading = false
          this.$parent.initData()
        }).catch(err => {
          this.loading = false
          //console.log(err.response.data.message)
        })
      },
      resetForm(formName) {
          this.$refs[formName].resetFields();
      }
    }

}
</script>
<style>

</style>