<template>
  <el-dialog :visible.sync="dialog" :close-on-click-modal="false" :before-close="cancel" :title="title2" append-to-body  @close="cancel">
    <el-form ref="form" :model="form" :rules="rules" size="small" label-width="88px">
      <el-form-item label="项目名称" prop="item_name">
        <el-input v-model="form.item_name" type="text" auto-complete="on" style="width: 370px;" />
      </el-form-item>
      <el-form-item label="项目状态" prop="item_status">
        <el-select v-model="form.item_status" placeholder="" style="width: 370px;" :disabled=isAdd>
          <el-option label="已完成" :value='1' ></el-option>
          <el-option label="未完成" :value='0' ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="项目图片">
        <el-upload
          action
          ref="upload"
          list-type="picture-card"
          accept=".jpeg,.jpg,.png"    
          :limit="1"
          :on-exceed="handleExceed"
          :before-remove="beforeRemove"
          :on-remove="handleRemove"
          :on-preview="handlePictureCardPreview"    
          :before-upload="beforeUpload"
          :file-list="fileList"
        >
        <i slot="default" class="el-icon-plus"/>
        <el-dialog :append-to-body="true" :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" >
        </el-dialog>
        <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
      </el-upload>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="cancel">取消</el-button>
      <el-button :loading="loading" type="primary" @click="submitUpload()">确定</el-button>
    </span>
  </el-dialog>
</template>
<script>
import { addProject, editProject } from '@/api/schedule/schedule'
export default {
  props: {
    isAdd: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      dialog: false,
      title2: "新增项目",
      dialogImageUrl: "",
      fileList: [],
      dialogVisible: false,
      headers: {},
      files: '',
      fileName: '',
      loading: false,
      form: { id: '', item_name: '', item_status: '' }, 
      trigger: false,
      rules: {
        item_name:
        [
          { required: true, message: '请输入项目名称', trigger: 'blur' },
        ],
        item_status: 
        [
          { required: true, message: '请选择项目状态', trigger: 'blur' },
        ]
      }, 
    }
  },
  methods: {
    /*
      关于上传的函数

    */
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    handleRemove(file, fileList) {
      this.fileName = ''
      this.trigger = !this.trigger
    },
    beforeRemove(file, fileList) {
      if (this.trigger) {
        return this.$confirm(`确定移除 ${ file.name }？`);
      } else {
        this.trigger = true
        return false
      }
    },
    
    beforeUpload(file) {
      this.files = file;
      const extension = file.name.split('.')[1] === 'jpg'
      const extension2 = file.name.split('.')[1] === 'png'
      const isLt2M = file.size / 1024 / 1024 < 5
      if (!extension && !extension2) {
          this.$message.warning('上传模板只能是 jpg、png格式!')
          return
      }
      if (!isLt2M) {
          this.$message.warning('上传模板大小不能超过 5MB!')
          return
      }
      this.fileName = file.name;
      return false // 返回false不会自动上传
    },

    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },

    submitUpload() {
      if(this.fileName == ""){
        this.$message.warning('请选择要上传的文件！')
        return false
      }
      this.$refs['form'].validate((valid) => {
        if (valid) {
          this.loading = true
          if (this.isAdd) {
            this.doAdd()
          } 
          else {
            this.doEdit()
          }
          this.resetForm()
        } else {
          return false
        }
      })
    },
    doAdd() {
      var token = sessionStorage.getItem('token'); // 获取token验证
      let requestConfig = {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Basic ${new Buffer(token).toString('base64')}`
        }
      }
      let fileFormData = new FormData();
      fileFormData.append('item_name', this.form.item_name)
      fileFormData.append('item_status', this.form.item_status)
      fileFormData.append('file', this.files)
      addProject(fileFormData, requestConfig).then(res => {
        this.dialog = false
        this.$notify({
          title: '添加成功',
          type: 'success',
          duration: 2500
        })
        this.$parent.initdata()
        this.loading = false
      }).catch(err => {
        this.loading = false
      })
    },
    doEdit() {
      console.log('fklsdfjk')
      var token = sessionStorage.getItem('token'); // 获取token验证
      let requestConfig = {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Basic ${new Buffer(token).toString('base64')}`
        }
      }
      let fileFormData = new FormData();
      fileFormData.append('id', this.form.id)
      fileFormData.append('item_name', this.form.item_name)
      fileFormData.append('item_status', this.form.item_status)

        // 先判断图片是否重新上传
      if(this.files === null){
        console.log(tljlk)
      }
      else{
        fileFormData.append('file', this.files)
      }      
      editProject(fileFormData, requestConfig).then(res => {
          this.dialog = false
          this.$notify({
            title: '修改成功',
            type: 'success',
            duration: 2500
          })
          this.$parent.initdata()
          this.loading = false
      }).catch(err => {
        this.loading = false
      })

    },

    resetForm() {
      this.fileList = []
      this.files = '',
      this.fileName = '',
      this.$refs.form.resetFields()
      this.$refs.upload.clearFiles()
    },

    cancel() {
      this.dialog = false
      this.resetForm()
    },
  } ,  
}
</script>
<style>

</style>
