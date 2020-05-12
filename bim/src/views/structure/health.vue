<template>
  <div class="app-container">
    <el-row :gutter="20" class="tree-content">
      <!--侧边树形结构-->
      <el-col :xs="9" :sm="6" :md="4" :lg="4" :xl="4" class="box-container">
        <div class="head-container">
          <el-input
            v-model="deptName"
            clearable
            size="small"
            placeholder="输入设施名搜索"
            prefix-icon="el-icon-search"
            class="filter-item"
            @input="getDeptDatas"
          />
        </div>
        <el-tree
          highlight-current
          :data="structureData"
          :props="defaultProps"
          :expand-on-click-node="false"
          default-expand-all
          @node-click="handleNodeClick"
        />
      </el-col>
       
      <!--用户数据-->
      <el-col :xs="6" :sm="8" :md="9" :lg="9" :xl="9" style="border-right: 0px solid #eee;height: 100%">
        <!--工具栏-->
        <div class="head-container" align="right" style="padding: 20px">
          <el-upload
            class="upload-demo"
            action="http://127.0.0.1:5000/upload/img"
            :on-preview="handlePreview"
            :show-file-list="false"
            :data="{'test':'123'}"
            :on-success="handleUploadSuccess">
            <el-button
              slot="default"
              class="filter-item"
              type="primary"
              size="mini"
            >
              更换图片
            </el-button>
          </el-upload>
        </div>
        <div class="img-div">
          <img v-if="trigger" :src="imagePath" title="无此图片" >
          <span v-else>
            点击左边选项
          </span>
        </div>
      </el-col>
      <el-col :xs="9" :sm="10" :md="11" :lg="11" :xl="11">
        <!--工具栏-->
        <div style="width: 100%" align="center">
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
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Treeselect from '@riophae/vue-treeselect'
import { mapGetters } from 'vuex'
import { getTree } from '@/api/structure/imagePath';
import '@riophae/vue-treeselect/dist/vue-treeselect.css'

export default {
  name: 'Health',
  components: { Treeselect },
  computed: {
    ...mapGetters([
      'baseApi',
      'imageApi'
    ])
  },
  data() {
    return {
      deptName: '', imagePath: '', trigger: false,
      structureData:  [ ],
      defaultProps: { children: 'children', label: 'label' },
    }
  },
  created() {
    this.$nextTick(() => {
      this.getDeptDatas()
      // this.crud.toQuery()
    })
  },
  mounted: function() {
    const that = this
    window.onresize = function temp() {
      that.height = document.documentElement.clientHeight - 180 + 'px;'
    }
  },
  methods: {
    getDeptDatas() {
      let param = { belong: '健康监测系统预留件' }
      getTree(param).then(res => {
        this.structureData.push(res.data)
      })
    },
    handleNodeClick(data) {
      if(data.id !== 0) {
        this.trigger = true
        // console.log(data)
        this.imagePath = this.imageApi + '/health/' + data.path
      }
    },
    handlePreview() {
    },
    handleUploadSuccess(res) {
    },
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
      padding: 20px;
      border: 1px solid #eee
    }

    img {
      width: 100%;
    }
  }
</style>
