<template>
  <div class="app-container">
    <div class="head-container">
        <div>
          <el-upload
            class="upload-demo"
            action="http://127.0.0.1:5000/secmanager/test"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            multiple
            :on-exceed="handleExceed">
            <img style="width: 79%" :src="imageApi + '/bridge_img/1.jpg'" title="点击上传头像" class="avatar">
            <!-- <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
          </el-upload>
          <h1>上传视频</h1>
          <el-upload
            class="upload-demo"
            action="http://127.0.0.1:5000/secmanager/test"
            :on-preview="handlePreview"
            list-type="picture-card"
            :on-success="handleAvatarSuccess">
            <i slot="default" class="el-icon-plus"></i>
            <!-- <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
          </el-upload>
          <video
            src="http://127.0.0.1:5000/static/test.mp4"
            controls="controls"
            style="width: 200px"
            align="center">
              您的浏览器不支持视频播放
          </video>
          <br>
          <br>

          <el-input
            placeholder="输入关键字进行过滤"
            v-model="filterText"
            style="width: 300px;">
          </el-input>

          <el-tree
            class="filter-tree"
            :data="treedata"
            :props="defaultProps"
            default-expand-all
            :filter-node-method="filterNode"
            ref="tree">
          </el-tree>






        </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import { loadTree } from '@/api/operation/secmanager'
export default {
  data() {
    return {
      fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}, {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}],

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
    this.loadTree()
  },
  computed: {
    ...mapGetters([
      'baseApi',
      'imageApi'
    ])
  },
  methods: {
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