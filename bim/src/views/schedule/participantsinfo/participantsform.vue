<template>
  <div>
    <el-dialog append-to-body  :close-on-click-modal="false"  :before-close="cancel" :visible.sync= "dialog"
        :title="isAdd ? '新增参建人员信息' : '编辑参建人员信息'" width="500px"  @close="cancel">
      <el-form ref="form" :inline="true" :model="form" :rules="rules" size="small" label-width="80px">
        <el-form-item label="人员姓名" prop="participants_name">
          <el-input v-model="form.participants_name" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="人员性别" prop="participants_sex">
          <el-select v-model="form.participants_sex" placeholder="" style="width: 300px;">
            <el-option label="男" :value='1'></el-option>
            <el-option label="女" :value='0'></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="联系电话" prop="participants_tel">
          <el-input v-model="form.participants_tel" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="从业资质" prop="participants_qualification">
          <el-input v-model="form.participants_qualification" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="岗位状态" prop="participants_work_status">
          <el-select v-model="form.participants_work_status" placeholder="" style="width: 300px;">
            <el-option label="在岗" :value='1'></el-option>
            <el-option label="离岗" :value='0'></el-option>
          </el-select>
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
import {addParticipantsinfo, editParticipantsinfo } from "@/api/schedule/paticipantsinfo"
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
        participants_name: '',
        participants_sex: '',
        participants_tel: '',
        participants_work_status: '',
        participants_qualification: ''
      },
      rules: {
        participants_name: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        participants_sex: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        participants_tel: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        participants_work_status: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],
        participants_qualification: [
            { required: true, message: '请输入用户名称', trigger: 'blur' },
        ],       
      },
    }
  },
  methods: {
    cancel() {
      this.resetForm("form")
    },
    resetForm(val){
      this.dialog = false
      this.$refs[val].resetFields();
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
      addParticipantsinfo(this.form).then(res => {
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
      editParticipantsinfo(this.form).then(res => {
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