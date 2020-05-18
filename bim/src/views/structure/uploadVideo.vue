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
          action="#"
          accept=".mp4"
          :limit="1"
          :on-change="onChange"
          :on-exceed="handleExceed"
          :file-list="fileList"
          :auto-upload="false">
          <el-button slot="trigger" size="small" type="success" >选取文件</el-button> 
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
import { uploadVideo } from '@/api/structure/uploadimage'
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
      dialog: false, fileList: [], file: null,
      form: { position: null },
      rules: {
        position: [
          { required: true, message: '请选择视频展示位置', trigger: 'blur' },
        ]
      }
    };
  },
  methods: {
    onChange(file, fileList) {
      this.fileList = fileList
      //这里做一些文件控制，注意：就算一次选取多个文件，这里依旧会执行多次
    },
    submitUpload() {
      if (this.fileList === null || this.fileList.length == 0) {
        this.$message.warning('请选择要上传的文件！')
        return
      }
      if (this.form.position === null) {
        this.$message.warning('请选择视频所要展示位置')
      } else {
        var formData = new FormData();
        formData.append('file', this.fileList[0].raw)
        formData.append('id', this.id)
        formData.append('belong', this.belong)
        formData.append('position', this.form.position)
        uploadVideo(formData).then(res => { //手动上传貌似无法触发成功或失败的钩子函数，因此这里手动调用 
      　　  this.onSuccess(res.data) 
        }).catch(err => {
        　　console.log(err)
        　　this.onError()
        })
      }
    },
    cancel() {
      this.$refs.upload.clearFiles()
      this.form.position = null
      this.dialog = false
    },
    onSuccess(data) {
      this.$refs.upload.clearFiles()
      this.$notify({
        title: '上传成功',
        type: 'success',
        duration: 2500
      })
      this.dialog = false
      this.$nextTick(() => {
        this.$parent.refresh(data)
      })
    },
    handleExceed() {
      this.$message.warning(`当前限制选择 1 个文件，请先删除后再上传`);
    }
  }
}
</script>
