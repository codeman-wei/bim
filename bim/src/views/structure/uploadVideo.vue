<template>
  <el-dialog append-to-body :close-on-click-modal="false" :before-close="cancel" :visible.sync="dialog" title = "新增视频" width="35%" @close="cancel">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="展示位置:" prop="name">
        <el-radio-group v-model="form.position" size="small">
          <el-radio-button label="up">上</el-radio-button>
          <el-radio-button label="bottom">下</el-radio-button>
          <el-radio-button label="left">左</el-radio-button>
          <el-radio-button label="right">右</el-radio-button>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="视频:">
        <el-upload
          class="upload-demo"
          ref="upload"
          action="http://127.0.0.1:5000/upload/video"
          accept=".mp4"
          :limit="1"
          :data="form"
          :on-exceed="handleExceed"
          :on-success="handleSuccess"
          :file-list="fileList"
          :auto-upload="false">
          <el-button slot="trigger" size="small" type="success">选取文件</el-button> 
        </el-upload>
      </el-form-item>
    
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button type="text" @click="cancel">取消</el-button>
      <el-button style="margin-left: 10px;" size="small" type="primary" @click="submitUpload">上传</el-button>
    </span>
  </el-dialog>
</template>
<script>
const token = sessionStorage.getItem('token')
  export default {
    props: {
      id: {
        type: Number,
        required: true
      },
      belong: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        dialog: false, fileList: [],
        form: { id: null, position: null, belong: null },
        rules: {
          position: [
            { required: true, message: '请选择视频展示位置', trigger: 'blur' },
          ]
        }
      };
    },
    methods: {
      submitUpload() {
        if (this.form.position === null) {
          this.$message({
            message: '请选择视频所要展示位置',
            type: 'warning'
          })
        } else {
          this.form['id'] = this.id
          this.form['belong'] = this.belong
          this.$refs.upload.submit();
        }
      },
      cancel() {
        this.$refs.upload.clearFiles()
        this.dialog = false
      },
      handleSuccess() {
        this.$refs.upload.clearFiles()
        this.$notify({
          title: '上传成功',
          type: 'success',
          duration: 2500
        })
        this.dialog = false
      },
      handleExceed() {
        this.$message.warning(`当前限制选择 1 个文件，请先删除后再上传`);
      }
    }
  }
</script>
