<template>
  <div class="app-container">
    <div class="boader-container">
      <!-- 头部面包屑和按钮 -->
      <div class="option-bar">
          <el-breadcrumb style="margin-top: 10px" separator-class="el-icon-arrow-right">
            <el-breadcrumb-item >
              <i class="el-icon-sort-up"/>
              <label class="text-button" @click="rollbackTo(breadcrumbList.length-2)">返回上一级</label>
            </el-breadcrumb-item>
            <el-breadcrumb-item v-for="(item, index) in breadcrumbList" :key="item.id">
              <span class="text-button" @click="rollbackTo(index)">{{ item }}</span>
            </el-breadcrumb-item>
          </el-breadcrumb>
        <div>
          <el-button :disabled="cuStatus !== 0" size="small" icon="el-icon-folder-add" type="primary" plain @click="addFold">新建文件夹</el-button>
          <el-button :disabled="selections.length === 0" size="small" icon="el-icon-delete" type="primary" plain>删除</el-button>
          <el-button :disabled="cuStatus !== 0" size="small" icon="el-icon-upload2" type="primary" plain>上传</el-button>
          <el-button :disabled="cuStatus !== 0" size="small" icon="el-icon-download" type="primary" plain>下载</el-button>
        </div>
      </div>
      <!-- 文件展示列表 -->
      <el-table
        ref="table"
        size="medium"
        :header-cell-style="{background:'#eef1f6',color:'#606266'}"
        :data="data"
        :highlight-current-row="true"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange"
        @current-change="handleCurrentChange"
        @row-dblclick="handleRowDblclick"
        @cell-mouse-enter="handleCellMouseEnter"
        @cell-mouse-leave="handleCellMouseLeave"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="fileName" label="文件名" width="500px">
          <template slot-scope="props">
            <img :src="props.row.isFold ? '/static/images/下载.png':'/static/images/file.png'" style="vertical-align:middle">
            <span :ref="'text'+props.row.id" style="padding: 0 10px;" @click="handleTextClick(props.row)">{{ props.row.fileName }}</span>
            <!-- 文件名修改框 -->
            <div :ref="props.row.id" style="display: none">
              <el-input  v-model="rename" style="display: inline-block;width: 200px;" size="small"/>
              <!-- 编辑按钮 -->
              <span class="tag-span" @click="comfirmRename">
                <i class="el-icon-check"></i>
              </span>
              <span class="tag-span" @click="cancelRename">
                <i class="el-icon-close"></i>
              </span>
            </div>
            <div :ref="'op' + props.row.id" class="row-operation">
              <span  class="text-button">
                <i class="el-icon-delete"/>
                删除
              </span>
              <span class="text-button">
                <i class="el-icon-download"/>
                下载
              </span>
            </div>
          </template>
        </el-table-column>
        <el-table-column prop="fileSize" label="大小" />
        <el-table-column prop="creater" label="创建者" />
        <el-table-column prop="time" label="创建时间" />
      </el-table>
      <div style="padding: 20px;font-size: 14px">
        <span>全部 <el-tag type="info">{{ this.data.length }}</el-tag> 个, 已选择 <el-tag type="info">{{ this.selections.length }}</el-tag> 个</span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'test',
  data() {
    return {
      current: null, selections: [], rename: null, breadcrumbList: ["首页"],
      cuStatus: 0,
      data: [
        { id: 0, fileName: '我是文件夹', fileSize: '--', creater: '管理员', isFold: true, time: '2020-04-01 12:12:12' },
        { id: 1, fileName: '我是一个文件.png', fileSize: '22.2kb', creater: '管理员', isFold: false, time: '2020-04-01 12:12:12' }
      ],
    }
  },
  methods: {
    handleSelectionChange(val) {
      this.selections = val   
    },
    handleTextClick(val) {
      if (this.current !== null && val.id === this.current.id) {
        this.rename = val.fileName
        this.changeEditShow(true)
        this.cuStatus = 2
      }
    },
    handleCurrentChange(val) {
      // 当前如果是属于添加新文件夹状态，这时候点击其他行代表取消新建
      // 这样做主要是为了防止文件名重复，没有其他更好办法
      if (this.cuStatus === 1) {
        this.data.splice(0, 1)
        this.cuStatus = 0
      }
      // 某行处于编辑状态，当点击其他行，编辑状态取消
      if (this.current !== null) {
        this.changeEditShow(false)
      }
      this.current = val
      this.$refs.table.clearSelection();
      this.$refs.table.toggleRowSelection(val);
    },
    handleRowDblclick(row, column, event) {
      if (row.isFold) {
        this.breadcrumbList.push(row.fileName)
        this.data = [
          { id: 0, fileName: '我是一个音乐文件.mp4', fileSize: '--', creater: '管理员', isFold: false, time: '2020-04-01 12:12:12' },
          { id: 1, fileName: '我是一个视频.mp4', fileSize: '4.2M', creater: '管理员', isFold: false, time: '2020-04-01 12:12:12' }
        ]
      }
    },
    handleCellMouseEnter(row) {
       this.$refs['op' + row.id].style.display = 'inline'
    },
    handleCellMouseLeave(row) {
       this.$refs['op' + row.id].style.display = 'none'
    },
    comfirmRename() {
      if (this.checkExist()) {
        this.current.fileName = this.rename
        this.cuStatus = 0
        this.changeEditShow(false)
      }
    },
    cancelRename(){
      // 当前如果是属于添加新文件夹状态，点击取消框代表取消新建，这样做主要是为了防止文件名重复，没有其他更好办法
      if (this.cuStatus === 1) {
        this.data.splice(0, 1)
      } else {
        this.changeEditShow(false)
      }
      this.cuStatus = 0
      this.rename = null
    },
    changeEditShow(isEdit) {
      this.$refs[this.current.id].style.display = isEdit ? 'inline':'none'
      this.$refs['text' + this.current.id].style.display = isEdit ? 'none':'inline'
    },
    rollbackTo(index) {
      this.breadcrumbList = index >= 0 ? this.breadcrumbList.slice(0, index+1) : this.breadcrumbList
      this.data = [
        { id: 1, fileName: '我是文件夹', fileSize: '--', creater: '管理员', isFold: true, time: '2020-04-01 12:12:12' },
        { id: 2, fileName: '我是一个文件.png', fileSize: '22.2kb', creater: '管理员', isFold: false, time: '2020-04-01 12:12:12' }
      ]
    },
    addFold() {
      const fold = { id: this.data.length, fileName: '新建文件夹', fileSize: '--', creater: '管理员', isFold: true, time: '2020-04-01 12:12:12' }
      this.data.splice(0, 0, fold)
      this.$refs.table.setCurrentRow(fold)
      this.$nextTick(function(){
        this.handleTextClick(fold)  //输出：修改后的值
        this.cuStatus = 1
      })
    },
    checkExist() {
      return this.data.every(item => {
        if (item.fileName === this.rename && item.id !== this.current.id) {
          this.$message.error("同级中存在同名文件,文件名不能重复")
          return false
        }
        return true
      })
    }
  }
}
</script>
<style lang="scss" scoped>
  .app-container {
    padding: 10px;
    .boader-container {
      border-radius: 10px;
      border: 1px dashed #ccc;
      padding: 10px;
      .option-bar {
        display: flex;
        justify-content:space-between;
        margin-bottom: 10px;
      }
      .tag-span {
        border: 2px solid #daebfe;
        text-align: center;
        color: #101010;
        background-color: #ebeef5;
        font-weight: 700;
        display: inline-block;
        width: 24px;
      }
      .text-button, .tag-span {
        cursor: pointer !important;
      }
      .row-operation {
        position: absolute;
        right: 40px;
        display: none;
        color: rgb(64, 158, 255);
        span {
          margin: 0px 5px;
          line-height: 2em;
        }
      }
    }
  }
  .table-head {
    color: gray;
  }
</style>
