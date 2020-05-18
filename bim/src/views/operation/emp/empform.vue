<template>
  <div>
    <el-dialog append-to-body  :close-on-click-modal="false"  :before-close="cancel" :visible.sync= "dialog"
        :title="isAdd ? '新增参建人员信息' : '编辑参建人员信息'" width="500px"  @close="cancel">
      <el-form ref="form" :inline="true" :model="form" :rules="rules" size="small" label-width="80px">
        <el-form-item label="人员姓名" prop="emp_name">
          <el-input v-model="form.emp_name" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="岗位证号" prop="emp_number">
          <el-input v-model="form.emp_number" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="联系电话" prop="emp_tel">
          <el-input v-model="form.emp_tel" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="所属部门" prop="emp_dept">
          <el-input v-model="form.emp_dept" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="所属职位" prop="emp_position">
          <el-input v-model="form.emp_position" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="岗位状态" prop="emp_work_status">
          <el-select v-model="form.emp_work_status" style="width: 300px;" placeholder="">
            <el-option label="在岗" :value='1'></el-option>
            <el-option label="离岗" :value='0'></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="工作职责" prop="emp_duty">
          <el-input v-model="form.emp_duty" style="width: 300px;" type="textarea"/>
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="cancel()">取消</el-button>
        <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import {addEmpInfo, editEmpInfo} from "@/api/operation/employee"
export default {
  props: {
    isAdd: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      loading: false,
      dialog: false,
      form: {
        id: '',
        project_id: '',
        emp_name: '',
        emp_number: '',
        emp_tel: '',
        emp_work_status: '',
        emp_dept: '',
        emp_position: '',
        emp_duty: ''
      },
      rules: {
        emp_name: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        emp_work_status: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        emp_duty: [
            { max: 100, message: '长度不得超过100个字', trigger: 'blur' },
        ],       
      },
    }
  },
  methods: {
    cancel() {
      this.resetForm("form")
    },
    resetForm(val){
      this.$refs[val].resetFields();
      this.dialog = false
    },
    doSubmit() {
      this.form['project_id'] = this.$parent.projectid
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
      addEmpInfo(this.form).then(res => {
        this.dialog = false
        this.resetForm('form')
        this.$notify({
          title: '添加成功',
          type: 'success',
          duration: 2500
        })
        this.loading = false
        this.$parent.initdata()
        this.$parent.initdata2()
      }).catch(err => {
        this.loading = false
      })
    },
    doEdit() {
      editEmpInfo(this.form).then(res => {
        this.resetForm('form')
        this.$notify({
          title: '修改成功',
          type: 'success',
          duration: 2500
        })
        this.loading = false
        this.$parent.initdata()
        this.$parent.initdata2()
      }).catch(err => {
        this.loading = false
      })
    },

  }
}
</script>
<style>

</style>