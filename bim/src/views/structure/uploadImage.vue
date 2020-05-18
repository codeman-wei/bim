<template>
  <el-dialog append-to-body :close-on-click-modal="false" :before-close="cancel" :visible.sync= dialog :title = "isAdd?'新增部件信息':'修改部件信息'" width="400" @close="cancel">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="部件名称" prop="name">
        <el-input type="text" v-model="form.name"  auto-complete="on" style="width: 370px;" />
      </el-form-item>
      <el-form-item label="部件详情">
        <el-input type="textarea" v-model="form.abstract" auto-complete="on" style="width: 370px;" ></el-input>
      </el-form-item>
      <el-form-item label="部件图片">
        <el-upload
          action="http://127.0.0.1:5000/upload/img"
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

import { upload, edit } from '@/api/structure/uploadimage'
export default {
    props: {
      isAdd: {
        type: Boolean,
        required: true
      },
      belong: {
        type: String,
        required: true
      }
    },
    data() {
      return {
          loading: false,
          files: '',
          dialogImageUrl: '',
          dialogVisible: false,
          fileName: '',
          trigger: false,
          fileList: [],
          dialog: false,
          form: { id: '', pid: '', name: '', abstract: '' }, 
          headers: {
            
          },
          rules: {
            name: [
              { required: true, message: '请输入部件名称', trigger: 'blur' },
            ]
          }, 
      }
    },
    methods: {
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
          this. trigger = true
          return false
        }
      },
      /*
        file.status ==> ready / success
      */
      beforeUpload(file) {
        this.files = file;
        const extension = file.name.split('.')[1] === 'jpg'
        const extension2 = file.name.split('.')[1] === 'png'
        const isLt2M = file.size / 1024 / 1024 < 5
        if (!extension && !extension2) {
            this.$message.warning('上传模板只能是 xls、xlsx格式!')
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

      cancel() {
          this.dialog = false
          this.resetForm()
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
        let fileFormData = new FormData(`Basic ${new Buffer(token).toString('base64')}`);
        fileFormData.append('imageName', this.form.name)
        fileFormData.append('imgaeAbstract', this.form.abstract)
        fileFormData.append('structName', this.belong)
        fileFormData.append('file', this.files)
        upload(fileFormData, requestConfig).then(res => {
          this.dialog = false
          this.resetForm()
          this.$notify({
            title: '添加成功',
            type: 'success',
            duration: 2500
          })
          this.$parent.getDeptDatas()
          this.loading = false
        }).catch(err => {
          this.loading = false
        })
      },
      resetForm() {
        this.fileList = []
        this.$refs.upload.clearFiles()
        this.trigger = false
        this.dialog = false
        this.form = { id: '', pid: '', name: '', abstract: '' }
      },
      doEdit() {
        var token = sessionStorage.getItem('token'); // 获取token验证
        let requestConfig = {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Basic ${new Buffer(token).toString('base64')}`
          }
        }    
        this.loading = false
        let fileFormData = new FormData();
        fileFormData.append('id', this.form.id)
        fileFormData.append('imageName', this.form.name)
        fileFormData.append('imgaeAbstract', this.form.abstract)
        fileFormData.append('structName', this.belong)
        //fileFormData.append('file', this.fileList[0])
        // 先判断图片是否重新上传
        if(this.files === null)
          console.log(tljlk)
        else
          fileFormData.append('file', this.files)
        edit(fileFormData, requestConfig).then(res => {
          this.dialog = false
          this.resetForm('form')
          this.$notify({
            title: '修改成功',
            type: 'success',
            duration: 2500
          })
          this.$parent.refresh(res.data)
          // this.$parent.getDeptDatas()

          this.loading = false
        }).catch(err => {
          this.loading = false
        })
      },
    }
}
</script>