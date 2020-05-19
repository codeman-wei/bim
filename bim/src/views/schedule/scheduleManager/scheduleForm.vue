<template>
  <el-dialog :visible.sync="dialog" :close-on-click-modal="false"  :before-close="cancel" :title="isAdd? '新增项目':'编辑项目'" 
    append-to-body width="500px" @close="cancel">
    <el-form ref="form" :model="form" :rules="rules" size="small" label-width="88px">
      <el-form-item label="施工流程" prop="sub_project_name">
        <el-input v-model="form.sub_project_name" type="text" auto-complete="on" style="width: 370px;" />
      </el-form-item>
      <el-form-item label="活动时间">
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.start_time" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">
          <div style="padding: 2px 13px;font-weight:bold">-</div>
        </el-col>
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.end_time" style="width: 100%;"></el-date-picker>
        </el-col>
      </el-form-item>                   
      <el-form-item label="当前状态" prop="sub_project_status">
        <el-select v-model="form.sub_project_status" placeholder="" style="width: 370px;" :disabled=isAdd>
          <el-option label="已完成" :value="1"></el-option>
          <el-option label="未完成" :value="0"></el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="text" @click="cancel">取消</el-button>
      <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
    </div>
  </el-dialog>
</template>
<script>
import { addsubProject, editsubProject } from "@/api/schedule/scheduleInfo"
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
        sub_project_name: '',
        start_time: '',
        end_time: '',
        sub_project_status: '',
        project_id: ''
      },
      rules: {
        sub_project_name: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        start_time: [
            { required: true, message: '请选择开始时间', trigger: 'blur' },
        ],
        end_time: [
            { required: true, message: '请选择预计完成时间', trigger: 'blur' },
        ], 
      },
    }
  },
  methods: {
      cancel() {
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
      addsubProject(this.form).then(res => {
        this.dialog = false
        this.$notify({
          title: '添加成功',
          type: 'success',
          duration: 2500
        })
        this.loading = false
        this.resetForm('form')
        this.$parent.initdata2()
      }).catch(err => {
        this.loading = false
      })
    },
    doEdit() {
      editsubProject(this.form).then(res => {
        
        this.$notify({
          title: '修改成功',
          type: 'success',
          duration: 2500
        })
        this.loading = false
        this.resetForm('form')
        this.$parent.initdata2()
      }).catch(err => {
        this.loading = false
      })
    },
    cancel() {
      this.resetForm("form")
    },
    resetForm(val){
      this.dialog = false
      this.$refs[val].resetFields();
    },
      
  }
}
</script>
<style>

</style>