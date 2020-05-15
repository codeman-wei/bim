<template>
  <div class="app-container">
    <el-row :gutter="20" class="tree-content">
      <!--侧边树形结构-->
      <el-col :xs="8" :sm="8" :md="6" :lg="6" :xl="6" class="box-container">
        <div class="head-container">
          <el-button class="filter-item" type="primary" icon="el-icon-plus" size="mini" @click="add">新增</el-button>
          <el-input
            v-model="deptName"
            clearable
            size="small"
            placeholder="输入设施名搜索"
            prefix-icon="el-icon-search"
            class="filter-item"
          />
        </div>
        <el-tree
          style="overflow:hidden"
          highlight-current
          :data="structureData"
          :props="defaultProps"
          :expand-on-click-node="false"
          default-expand-all
          @node-click="handleNodeClick"
          :filter-node-method="filterNode"
          ref="tree"
        />
      </el-col>
       
      <!--用户数据-->
      <el-col :xs="8" :sm="8" :md="9" :lg="9" :xl="9" style="border-right: 1px dotted #eee;padding: 10px">
        <!--工具栏-->
        <div align="right">
          <!--搜索框 新增框-->
          <el-button class="filter-item" type="primary" icon="el-icon-upload" size="mini" @click="uploadimage" >编辑</el-button>
        </div>
        <div class="img-div">
          <img  v-if="trigger" :src="imagePath"  width="100%">
          <span v-else>
            点击左边选项
          </span>
        </div>
      </el-col>
      <el-col :xs="8" :sm="8" :md="9" :lg="9" :xl="9" style="padding: 10px">
        <!--工具栏-->
        <div class="" align="right">
          <!--搜索框 新增框-->
          <el-button class="filter-item" type="primary" icon="el-icon-upload" size="mini" @click="uploadvideo" >导入</el-button>
        </div>
        <div class="video-div">
          <img v-if="trigger" :src="imagePath" title="无此图片" width="100%">
          <span v-else>
            点击左边选项
          </span>
        </div>
        <!-- <div style="width: 100%" align="center">
          <div style="display: flex;justify-content: space-around; padding: 20px">
            <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-left"></el-button>
            <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-top"></el-button>
            <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-right"></el-button>
            <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-bottom"></el-button>
          </div>
          <video
            src="http://127.0.0.1:5000/static/test.mp4"
            controls="controls"
            style="max-height: 500px"
            align="center">
              您的浏览器不支持视频播放
          </video>
        </div> -->
      </el-col>
    </el-row>
    <uploadImage ref="image" :isAdd="isAdd" :belong="belong"/>
    <uploadVideo ref="video"  />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import uploadImage from '@/views/structure/uploadImage'
import uploadVideo from '@/views/structure/uploadVideo'
import { getTree } from '@/api/structure/imagePath';

export default {
  name: 'Health',
  components: {
    "uploadImage": uploadImage,
    "uploadVideo": uploadVideo,
  },
  created() {
    this.$nextTick(() => {
      this.getDeptDatas()
    })
  },
  data() {
    return {
      belong: "健康监测系统预留件",
      deptName: '', imagePath: '', imageName: '', trigger: false, isAdd:true,
      structureData:  [ ],
      defaultProps: { children: 'children', label: 'label' },
    }
  },
  computed: {
    ...mapGetters([
      'baseApi',
      'imageApi'
    ])
  },
  methods: {
    getDeptDatas() {
      let param = { belong: this.belong }
      getTree(param).then(res => {
        this.structureData = res.data
      })
    },
    handleNodeClick(data) {
      if(data.id !== 0) {
        this.trigger = true
        this.imageName = data.imageName
        // console.log(data)
        this.imagePath = this.imageApi + data.path
      }
    },
    add(){
      this.isAdd = true
      this.$refs.image.dialog = true
    },
    uploadimage() {
      this.isAdd=false
      this.$refs.image.dialog = true
    },
    uploadvideo() {
      this.$refs.video.dialog = true
    },
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    }
  }
}
</script>

<style scoped lang="scss">
  .tree-content {
    height: 100%;
    border: 1px solid #eee;

    .box-container {
      padding: 10px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }

    .el-col {
      height: 100%;
    }

    .img-div {
      text-align: center;
      padding: 7px;
      margin-top: 20px;
      border: 1px solid #eee
    }

    .video-div {
      margin-top: 15px;
      padding: 15px 20px;
    }

    img {
      width: 100%;
    }
  }
</style>
