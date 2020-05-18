<template>
  <div class="app-container">
    <div class="head-container">
        <div>
          <el-upload
            class="upload-demo"
            action="http://127.0.0.1:5000/upload/file"
            multiple
            :limit="5"
            :on-change="onChange"
            :file-list="fileList"
            :auto-upload="false"
            :on-exceed="handleExceed">
            <!-- <img style="width: 79%" :src="imageApi + '/bridge_img/1.jpg'" title="点击上传头像" class="avatar"> -->
            <el-button slot="default" size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
            <el-button size="small" type="success" @click="submitUpload">上传服务器</el-button>
          <!-- <h1>上传视频</h1>
          <el-upload
            class="upload-demo"
            action=""
            :on-preview="handlePreview"
            list-type="picture-card"
            :on-success="handleAvatarSuccess">
            <i slot="default" class="el-icon-plus"></i>
          </el-upload> -->
          <!-- <video
            src="http://127.0.0.1:5000/static/test.mp4"
            controls="controls"
            style="width: 200px"
            align="center">
              您的浏览器不支持视频播放
          </video> -->
          <br>
          <br>

          <el-input
            placeholder="输入关键字进行过滤"
            v-model="filterText"
            style="width: 300px;">
          </el-input>
<!-- 
          <el-tree
            class="filter-tree"
            :data="treedata"
            :props="defaultProps"
            default-expand-all
            :filter-node-method="filterNode"
            ref="tree">
          </el-tree> -->






        </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

// import { loadTree } from '@/api/operation/secmanager'
import { uploadFiles } from '@/api/structure/uploadimage'
export default {
  data() {
    return {
      fileList: [],

      filterText: '',
      treedata: [],
        // [{
        //   id: 1,
        //   label: '健康监测系统预留件',
        //   children: [
        //     {
        //       id: 1,
        //       label: '鼓屿门水道桥道砟预埋镀锌钢管布置图',
        //     },
        //     {
        //       id: 2,
        //       label: '鼓屿门水道桥预留件M1布置图',
        //     },
        //     {
        //       id: 3,
        //       label: '鼓屿门水道桥预留件M2M6布置图',
        //     },
        //     {
        //       id: 4,
        //       label: '鼓屿门水道桥预留件M3M6布置图',
        //     },
        //     {
        //       id: 5,
        //       label: '鼓屿门水道桥预留件M4M5M6布置图',
        //     },            
         
        //   ]
        // }],
        defaultProps: {
          children: 'children',
          label: 'label'
        },
    }
  },
  watch: {
      filterText(val) {
        this.$refs.tree.filter(val);
      }
  },
  created() {
    // this.loadTree()
  },
  computed: {
    ...mapGetters([
      'baseApi',
      'imageApi'
    ])
  },
  methods: {
    onChange(file, fileList) { //这里做一些文件控制，注意：就算一次选取多个文件，这里依旧会执行多次
    　　let existFile = fileList.slice(0, fileList.length - 1).find(f => f.name === file.name)
    　　if (existFile) {
    　　　　this.$message.error('当前文件已经存在!');
    　　　　fileList.pop()
    　　}
    　　this.fileList = fileList
    },
    onRemove(file, fileList) {
    　　this.fileList = fileList
    },
    OnExceed(file, fileList) {
    　　this.$message.error(`最多只能上传5个文夹`);
    },

    submitUpload() {   //上传函数，如果把提交函数用在http-request钩子中，fileList多长就执行请求多少次接口，依旧是无法做到只请求一次上传多文件
    　　var formData = new FormData();  //  用FormData存放上传文件
        if (this.fileList === null || this.fileList.length == 0) {
          this.$message.warning('请选择要上传的文件！')
          return
        }
    　　this.fileList.forEach(file => { 
    　　　　　　formData.append(file.raw.name, file.raw); //此处一定是append file.raw 上传文件只需维护fileList file.raw.name要加上 
    　　}) 
       uploadFiles(formData).then(res => { //手动上传貌似无法触发成功或失败的钩子函数，因此这里手动调用 
    　　  this.onSuccess() 
       }).catch(err => {
      　　console.log(err)
      　　this.onError()
       })
    },
    onSuccess() {
      
      this.$notify({
        title: '上传成功',
        type: 'success',
        duration: 2500
      })
    },
    onError() {

    },
    loadTree() {
      loadTree().then(res =>{
        console.log(res)
        this.treedata.push(res.data)
      })
    },


    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },






    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    },
    handleAvatarSuccess(res, file) {
      console.log(res)
      // this.imageUrl = URL.createObjectURL(file.raw);
    },
  }
}
</script>