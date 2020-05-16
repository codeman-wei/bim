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
          <el-button class="filter-item" type="primary" icon="el-icon-upload" size="mini" @click="uploadimage" :disabled="!trigger">编辑</el-button>
        </div>
        <div class="img-div">
          <div v-if="trigger">
            <img  :src="imagePath"  width="100%" style="text-align: center;"> 
            <div class="content" align="center">
              <el-tag type="info">{{imageInfo.imageName}}</el-tag>
              <div style="text-indent: 2em;margin-top:10px;" v-if="imageInfo.abstract !== ''">
                {{imageInfo.abstract}}
                <!-- 平潭海峡公铁两用大桥啦！世界最长的跨海峡公铁两用大桥一一平潭海峡公铁两用大桥，目前公路部分主体工程已经全部完工，铁路部分最后一座铁路桥正在架梁铺轨。通车后，大桥作为京台高速的咽喉部分，将有力推进海峡两岸基础设施的联通。这里是世界三大风暴海域之一，一年中6级以上大风天超过300天这里无风也起浪水流速度相当于长江中下游洪峰这里小岛棋布、地质复杂坚硬如铁的光板岩石是打桩建墩者的噩梦..... -->
              </div>
              <div v-else style="margin-top:3px; font-weight:normal;">
                暂无说明，请添加
              </div>
            </div>
          </div>
          <div v-else style="">
            点击左边选项
          </div>

        </div>
      </el-col>
      <el-col :xs="8" :sm="8" :md="9" :lg="9" :xl="9" style="padding: 10px">
        <!--工具栏-->
        <div class="" align="right">
          <!--搜索框 新增框-->
          <el-button class="filter-item" type="primary" icon="el-icon-upload" size="mini" @click="uploadvideo" :disabled="!trigger" >导入</el-button>
        </div>
        <div class="video-div">
          <div v-if="trigger" >
            <video
              :src="videoPath"
              controls="controls"
              style="width: 100%"
              align="center">
                您的浏览器不支持视频播放
            </video>
            <div style="display: flex;justify-content: space-around; padding: 20px">
              <el-button :disabled="videoLeftPath === null" class="filter-item" size="mini" type="success" icon="el-icon-caret-left" @click="getVideoPath('left')"></el-button>
              <el-button :disabled="videoUpPath === null" class="filter-item" size="mini" type="success" icon="el-icon-caret-top" @click="getVideoPath('up')"></el-button>
              <el-button :disabled="videoRightPath === null" class="filter-item" size="mini" type="success" icon="el-icon-caret-right" @click="getVideoPath('right')"></el-button>
              <el-button :disabled="videoBottomPath === null" class="filter-item" size="mini" type="success" icon="el-icon-caret-bottom" @click="getVideoPath('bottom')"></el-button>
            </div>
          </div>
          <span v-else>
            点击左边选项
          </span>
        </div>
      </el-col>
    </el-row>
    <uploadImage ref="image" :isAdd="isAdd" :belong="belong"/>
    <uploadVideo ref="video" :id="selectId" :belong="belong" />
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
      belong: "健康监测系统预留件", selectId: 0,
      videoUpPath: '', videoPath: '',videoLeftPath: '', videoRightPath: '', videoBottomPath: '',
      deptName: '', imagePath: '', imageName: '', trigger: false, isAdd:true,
      structureData:  [ ],
      defaultProps: { children: 'children', label: 'label' },
      imageInfo: {}
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
      this.trigger = true
      this.selectId = data.id
      this.imageName = data.imageName
      this.imageInfo = data
      this.imagePath = this.imageApi + data.path
      this.videoUpPath = data.videoUpUrl
      this.videoLeftPath = data.videoLeftUrl
      this.videoRightPath = data.videoRightUrl
      this.videoBottomPath = data.videoBottomUrl
    },
    getVideoPath(pos) {
      switch (pos) {
        case 'left': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.videoLeftPath
          break;
        case 'up': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.videoUpPath
          break;
        case 'right': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.videoRightPath
          break;
        case 'bottom': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.videoBottomPath
          break;
      }
    },
    add(){
      this.isAdd = true
      this.$refs.image.dialog = true
    },
    uploadimage() {
      this.isAdd=false
      const _this = this.$refs.image
      _this.form = {
          id: this.imageInfo.id,
          name: this.imageInfo.imageName,
          abstract: this.imageInfo.abstract,
      }
      let tempDic = {
        name: this.imageInfo.imageName,
        url: this.imagePath
      }
      _this.fileList.push(tempDic)
      _this.fileName = this.imageInfo.imageName
      _this.dialog = true
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
      padding: 7px;
      margin-top: 20px;
      border: 1px solid #eee
    }

    .video-div {
      padding: 7px;
      margin-top: 20px;
      border: 1px solid #eee
    }

    img {
      width: 100%;
    }
    .content {
      margin-top: 15px;
      font-weight: bold;
      font-size: 15px;
      font-family: Arial, Helvetica, sans-serif;
    }
  }
</style>
