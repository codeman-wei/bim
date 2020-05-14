<template>
  <div class="bridgesynthesis-info">
    <el-row :gutter="20" class="tree-content">
      <!--侧边树形结构-->
      <el-col :xs="8" :sm="8" :md="6" :lg="6" :xl="6">
        <div class="">
           <!--搜索框 新增框-->
          <el-input placeholder="输入设施名搜索" v-model="filterText" prefix-icon="el-icon-search" size="mini" clearable style="width:250px;"> </el-input>
          <el-button class="filter-item" type="primary" icon="el-icon-plus" size="mini" @click="add">新增</el-button>
        </div>
        <el-tree
          class="filter-tree"
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
      <el-col :xs="8" :sm="8" :md="9" :lg="9" :xl="9">
        <div class="" align="right">
          <!--搜索框 新增框-->
          <el-button class="filter-item" type="primary" icon="el-icon-upload" size="mini" @click="uploadimage" >编辑</el-button>
        </div>

        <div class="img-div" >
          <img v-if="trigger" :src="imagePath"  width="100%">
          <span v-else>
            点击左边选项
          </span>
          <div class="title">

          </div>
          <div class="abstract">

          </div>
        </div>




      </el-col>
      <el-col :xs="8" :sm="8" :md="9" :lg="9" :xl="9" >
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
            <video
              src="http://127.0.0.1:5000/static/test.mp4"
              controls="controls"
              style="max-height: 500px"
              align="center">
                您的浏览器不支持视频播放
            </video>
            <div style="display: flex;justify-content: space-around; padding: 20px">
              <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-left"></el-button>
              <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-top"></el-button>
              <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-right"></el-button>
              <el-button class="filter-item" size="mini" type="success" icon="el-icon-caret-bottom"></el-button>
            </div>
          </div> -->
      </el-col>
    </el-row>
    <uploadImage ref="image" :isAdd="isAdd" :belong="belong"/>
    <uploadVideo ref="video"  />

  </div>
</template>
<script>
import { getTree } from '@/api/structure/imagePath';
import uploadImage from '@/views/structure/uploadImage'
import uploadVideo from '@/views/structure/uploadVideo'
import { mapGetters } from 'vuex'
export default {
  components: {
    "uploadImage": uploadImage,
    "uploadVideo": uploadVideo,
  },

  data() {
    return {
      filterText: '', imagePath: '', trigger: false, isAdd:true,
      structureData: [],
      defaultProps: { children: 'children', label: 'label' },
      belong: "桥梁综合接地"
    }
  },
  watch: {
    filterText(val) {
      this.$refs.tree.filter(val);
    }
  },
  computed: {
    ...mapGetters([
      'baseApi',
      'imageApi'
    ])
  },
  created() {
    this.$nextTick(() => {
      this.getDeptDatas()
    })
  },
  methods: {
    uploadimage() {
      this.isAdd=false
      this.$refs.image.dialog = true
    },
    uploadvideo() {
      this.$refs.video.dialog = true
    },
    getDeptDatas() {
      let param = { belong: this.belong}
      getTree(param).then(res => {
        this.structureData = res.data
      })
    },
    add(){
      this.isAdd = true
      this.$refs.image.dialog = true
    },
    handleNodeClick(data) {
      this.trigger = true
      this.imagePath = this.imageApi + '/health/' + data.path
      console.log(this.imagePath)
    },
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    handleUploadSuccess() {},
  }

}
</script>
<style>
  .bridgesynthesis-info {
    padding: 20px 20px;
  }
  .img-div {
    padding: 15px 20px;
    /* border: 1px solid #eee */
  }
  .video-div {
    padding: 15px 20px;
  }
  /* .head-container {
    margin-bottom: 10px;
  } */
</style>