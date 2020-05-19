<template>
  <div class="logs-info">
    <el-row style="margin:15px 10px;"> 
        <div style="float:left">
            <el-input v-model="keyword" clearable size="mini" placeholder="输入操作事件内容" style="width: 200px;"  class="filter-item" />
            <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="search">搜索</el-button>
            <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh" @click="reset">重置</el-button>

        </div>
        <div style="float:right">

        </div>
    </el-row>

    <div class="logs-table">
      <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55" align="center" header-align="center"> </el-table-column>
          <el-table-column prop="belong" label="所属模块" align="center" header-align="center"> </el-table-column>
          <el-table-column prop="reason" label="操作事件" align="center" header-align="center"> </el-table-column>
          <el-table-column prop="loginname" label="操作用户" align="center" header-align="center"> </el-table-column>
          <el-table-column prop="op" label="操作类型" align="center" header-align="center">
            <template slot-scope="scope">
                <el-tag :type="scope.row.op === 1 ? 'success' : 'primary'" disable-transitions>{{ scope.row.op === 1 ? '上传' : '修改' }}</el-tag>
            </template> </el-table-column>
          <el-table-column prop="updatetime" label="修改时间" align="center" header-align="center">
            <template :show-overflow-tooltip="true" slot-scope="scope">
              <span>{{ parseTime2(scope.row.updatetime) }}</span>
            </template>   
          </el-table-column>
      </el-table>
      
      <div class="block">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="page"
          :page-sizes="[10, 20, 30, 40]"
          :page-size="size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
import { getlogs } from '@/api/structure/logs'
import { parseTime2 } from '@/utils/index'
export default {
  data(){
    return {
      size: 10,
      page: 1,
      total: 0,
      tableData: [],
      keyword: ''
    }
  },
  created() {
    this.initdata()
  },
  methods: {
    parseTime2,
    initdata(){
      const sort = 'id,desc'
      let params = {
          page: this.page,
          size: this.size,
          sort: sort
      }
      if(this.keyword !== '') {
          params['keyword'] = this.keyword
      }
      getlogs(params).then(res=>{
        let { content, totalElements } = res.data
        this.total = totalElements
        this.tableData = content
      })
    },

    search() {
      this.page = 1
      this.initdata()
    },
    reset() {
      this.keyword = ""
      this.search()
    },

    handleSizeChange(val) {
        this.page = 1
        this.size = val
        this.initdata()
    },

    handleCurrentChange(val) {
      this.page = val
      this.initdata()
    },

    handleSelectionChange(val) {},
  }

}
</script>
<style>
  .logs-info {
    padding: 10px 25px;
  }
  .logs-table {
    margin-top: 20px;
  }
</style>