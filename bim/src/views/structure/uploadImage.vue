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
        <!-- 设置auto-upload = false 则 before-upload将不会触发-->
        <!-- 设置 :on-exceed="handleExceed"  -->
        <!-- 设置 before-remove 移除后触发-->
        <!-- 设置 on-remove 移除时触发-->
        <el-upload
          action="http://127.0.0.1:5000/upload/img"
          class="upload-demo"
          ref="upload"
          drag
          :auto-upload="false"
          :limit="1"
          :on-exceed="handleExceed"
          :on-remove="handleRemove"
          :before-remove="beforeRemove"
          :on-change="handleChange"
          accept=".jpeg,.jpg,.png" 
          >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
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

import { upload } from '@/api/structure/uploadimage'
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
          fileName: '',
          dialog: false,
          form: {
            name: '',
            abstract: ''
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
        console.log("hitei")
      },

      beforeRemove(file, fileList) {
        return this.$confirm(`确定移除 ${ file.name }？`);
      },
      /*
        file.status ==> ready / success
      */
      handleChange(file, fileList){
        if(file.status === 'ready')
        {
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
        }
      },

      cancel() {
          this.dialog = false
      },


      submitUpload() {
        const extension = this.fileName.split('.')[1] === 'jpg'
        const extension2 = this.fileName.split('.')[1] === 'png'
        if (!extension && !extension2) {
          return;
        }
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
        fileFormData.append('imageName', this.form.name)
        fileFormData.append('imgaeAbstract', this.form.abstract)
        fileFormData.append('structName', this.belong)
        fileFormData.append('file', this.files)
        upload(fileFormData, requestConfig).then(res => {
          this.dialog = false
          this.resetForm('form')
          this.$notify({
            title: '添加成功',
            type: 'success',
            duration: 2500
          })
          this.loading = false
        }).catch(err => {
          this.loading = false
          //console.log(err.response.data.message)
        })
      },


      resetForm() {
        this.dialog = false
        this.$refs['form'].resetFields()

      },
      doEdit() {
        console.log(this.isAdd)
        // edit(this.form).then(res => {
        //   this.resetForm()
        //   this.$notify({
        //     title: '修改成功',
        //     type: 'success',
        //     duration: 2500
        //   })
        //   this.loading = false
        //   this.$parent.init()
        // }).catch(err => {
        //   this.loading = false
        //   console.log(err.response.data.message)
        // })
      },
    }
}
</script>