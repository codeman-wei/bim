<template>
    <div class="app-container">
    <el-row :gutter="20" class="tree-content">
      <!--侧边树形结构-->
      <el-col :span="7" class="box-container">
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
      <el-col :span="17" style="padding: 10px">
        <!--工具栏-->
        <div align="right" style="margin-bottom: 10px">
          <!--新增框-->
          <el-button class="filter-item" type="primary" icon="el-icon-upload" size="mini" @click="uploadimage" :disabled="!trigger">编辑</el-button>
          <el-button class="filter-item" type="warning" icon="el-icon-video-camera-solid" size="mini" @click="showVideo" :disabled="!trigger">视频</el-button>
        </div>
        <div class="img-div">
          <div v-if="trigger" align="center">
            <img  :src="imagePath" style="text-align: center;width: 80%;"> 
            <div style="margin: 10px 0" align="center">
              <el-tag type="info">{{imageInfo.imageName}}</el-tag>
            </div>
            <div class="content" align='left'>
              <!-- <el-tag type="info">{{imageInfo.imageName}}</el-tag> -->
              <span v-if="imageInfo.abstract !== ''">
                {{imageInfo.abstract}}
                <!-- 平潭海峡公铁两用大桥啦！世界最长的跨海峡公铁两用大桥一一平潭海峡公铁两用大桥，目前公路部分主体工程已经全部完工，铁路部分最后一座铁路桥正在架梁铺轨。通车后，大桥作为京台高速的咽喉部分，将有力推进海峡两岸基础设施的联通。这里是世界三大风暴海域之一，一年中6级以上大风天超过300天这里无风也起浪水流速度相当于长江中下游洪峰这里小岛棋布、地质复杂坚硬如铁的光板岩石是打桩建墩者的噩梦..... -->
              </span>
              <span v-else style="">
                暂无说明，请添加
              </span>
            </div>
          </div>
          <div v-else style="">
            点击左边选项
          </div>

        </div>
      </el-col>
    </el-row>
    <uploadImage ref="image" :isAdd="isAdd" :belong="belong"/>
    <videoDialog ref="videoDialog" :data="imageInfo" :belong="belong" />
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import uploadImage from '@/views/structure/uploadImage'
import videoDialog from '@/views/structure/components/videoDialog'
import { getTree } from '@/api/structure/imagePath';

export default {
  name: 'ProtectiveScreen',
  components: {
    "uploadImage": uploadImage,
    "videoDialog": videoDialog
  },
  created() {
    this.$nextTick(() => {
      this.getDeptDatas()
    })
  },
  data() {
    return {
      belong: "桥梁供电、照明设施", selectId: 0,
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
  provide () {
    return {
      refresh: this.refresh
    }
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
    showVideo() {
      this.$refs.videoDialog.dialog = true
    },
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    refresh(data) {
      this.getDeptDatas()
      this.handleNodeClick(data)
    }
  }
}
</script>

<style scoped lang="scss">
  .tree-content {
    height: 100%;
    border: 0px solid #eee;

    .box-container {
      padding: 10px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }

    .el-col {
      min-height: 100%;
    }

    .img-div {
      padding: 7px;
      width: 100%;
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
      margin-top: 10px;
      // font-weight: bold;
      text-indent: 2em;
      // margin-top:10px;
      font-size: 14px;
      color: #aaa;
      font-family: Arial, Helvetica, sans-serif;
    }
  }
</style>
