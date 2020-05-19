<template>
  <div class="scheduleinfo">
    <el-row :gutter= "15">
      <el-col :xs="24" :sm="24" :md="8" :lg="8" :xl="8" >
        <el-card class="box-card" shadow="never">
            <div slot="header" class="clearfix">
              <span class="sys-span">施工项目列表</span>
            </div>
            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" >
                <el-table-column label="施工项目" width="200" :show-overflow-tooltip=true align="left" header-align="center">
                  <template slot-scope="scope">
                    <el-tooltip :content="scope.row.item_name" effect="light">
                    <span>{{scope.row.item_name | ellipsis }}</span>
                    </el-tooltip>
                  </template> 
                </el-table-column>
              <el-table-column label="项目状态" width="100" align="center" header-align="center"> 
                <template slot-scope="scope">
                  <el-tag :type="scope.row.item_status === 1 ? 'success' : 'primary'" disable-transitions>{{ scope.row.item_status === 1 ? '已完成' : '未完成' }}</el-tag>
                </template>
              </el-table-column>


                <el-table-column label="操作" width="150" align="center" header-align="center">
                <template slot-scope="scope">
                    <el-button size="mini" @click="handleLookupDetail(scope.$index, scope.row)">详情</el-button>
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
        </el-card>
      </el-col>
      <el-col :xs="24" :sm="24" :md="16" :lg="16" :xl="16">
        <el-card class="box-card" v-if="selected === false">
          <div slot="header" class="clearfix">
            <span class="sys-span">施工进度</span>
          </div>
          <div class="head-container">
            请选择施工项目
          </div>
        </el-card>
        <el-card class="box-card" shadow="never" v-if="selected === true">
          <div slot="header" class="clearfix">
            <span>施工进度</span>
            <el-divider direction="vertical" ></el-divider>
            <span>{{title}}</span>
          </div>
          <div class="head-container">
            <!-- 搜索 -->
            <div style="float:left;">
              <el-input v-model="keyword" clearable placeholder="输入关键字搜索" style="width: 200px;" class="filter-item" />
              <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="search">搜索</el-button>
              <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh" @click="reset">重置</el-button>

            </div>
            <div style="float:right;">
              <!-- 新增 -->
              <el-button class="filter-item" size="mini" type="primary" icon="el-icon-plus" @click="handleAdd" >新增</el-button>
              <!-- 删除 -->
              <el-button class="filter-item" size="mini" type="danger" icon="el-icon-delete"  @click="batchDELETE" :disabled="this.tableData2.length === 0">删除</el-button>
            </div>

            <el-table ref="multipleTable" :data="tableData2" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
              <el-table-column type="selection" width="55"> </el-table-column>
              <el-table-column prop="sub_project_name" label="施工流程"> </el-table-column>
              <el-table-column prop="start_time" label="开始时间" >
                  <template :show-overflow-tooltip="true" slot-scope="scope">
                      <span>{{ parseTime(scope.row.start_time) }}</span>
                  </template> 
              </el-table-column>
              <el-table-column prop="end_time" label="完成时间" >
                  <template :show-overflow-tooltip="true" slot-scope="scope">
                      <span>{{ parseTime(scope.row.end_time) }}</span>
                  </template>  </el-table-column>
              <el-table-column prop="sub_project_status" label="当前状态" > 
                <template slot-scope="scope">
                  <el-tag :type="scope.row.sub_project_status === 1 ? 'success' : 'warning'" disable-transitions>{{ scope.row.sub_project_status === 1 ? '已完成' : '未完成' }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="操作">
              <template slot-scope="scope">
                  <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
                  <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
            <div class="block">
              <el-pagination
                  @size-change="handleSizeChange2"
                  @current-change="handleCurrentChange2"
                  :current-page="page2"
                  :page-sizes="[10, 20, 30, 40]"
                  :page-size="size2"
                  layout="total, sizes, prev, pager, next, jumper"
                  :total="total2">
              </el-pagination>
            </div>
           </div>
        </el-card>
      </el-col>
    </el-row>
    <scheduleForm ref="scheduleForm" :isAdd=isAdd />
  </div>
</template>
<script>
import { getProjectScheduleInfo, getsubProjectById } from "@/api/schedule/scheduleInfo"
import scheduleForm from '@/views/schedule/scheduleManager/scheduleForm'
// import { deleteParticipantsinfo } from "@/api/schedule/paticipantsinfo"
// import participantform from '@/views/schedule/participantsinfo/participantsform'
// import {deleteBatchParticipantsinfo} from "@/api/schedule/paticipantsinfo"
import { parseTime } from '@/utils/index'
export default {
    components: {
        "scheduleForm": scheduleForm,
    },
    filters:{
      ellipsis(value){
          if (!value) return '';
          if (value.length > 12) {
              return value.slice(0,12) + '...'
          }
          return value
      }
    },
    data(){
      return {
        selected: false,
        isAdd:true,
        loading: false,
        tableData: [],
        tableData2: [],
        title: '',
        keyword: '',
        projectid: '',

        page: 1,
        size: 10,
        total: 0,

        page2: 1,
        size2: 10,
        total2: 0,

        multipleSelection: '',
      }
    },
    mounted() {
      this.initdata()
    },
    methods: {
      parseTime,
      initdata() {
        const sort = 'id,desc'
        let params = {
          page: this.page,
          size: this.size,
          sort: sort
        }
        getProjectScheduleInfo(params).then(res => {
          this.total = res.data.totalElements // 初始化时数据的总数
          this.tableData = res.data.content // 获取到的数据
        })
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

      handleLookupDetail(index, val){
        this.title = val.item_name
        this.projectid = val.id
        this.selected = true
        this.keyword = ""
        this.initdata2()
      },

      initdata2() {
        const sort = 'id,desc'
        let params = {
          page: this.page,
          size: this.size,
          projectid: this.projectid,
          sort: sort
        }
        if(this.keyword !== '') {
          params['sub_project_name'] = this.keyword
        }
        getsubProjectById(params).then(res => {
          this.tableData2 = res.data.content
          this.total2 = res.data.totalElements
        })
      },
      reset(){
        this.keyword =""
        this.initdata2()
      },
      search() {
        this.page = 1,
        this.initdata2()
      },

      handleSelectionChange(val){
        this.multipleSelection = val
      },

      handleAdd(){
        this.isAdd = true
        this.$refs.scheduleForm.dialog = true
        this.$refs.scheduleForm.form.sub_project_status = 0
      },




      batchDELETE() {
        // this.$confirm('您确定要批量删除吗?', '提示', {
        //   confirmButtonText: '确定',
        //   cancelButtonText: '取消',
        //   type: 'warning'
        //   }).then(() => {
        //       var ids = this.multipleSelection.map(item => item.id).join()//获取所有选中行的id组成的字符串，以逗号分隔
        //       let param = {
        //           "ids": ids
        //       }
        //       deleteBatchParticipantsinfo(param).then(res=> {
        //           this.$message({
        //               type: 'success',
        //               message: '删除成功!',
        //               duration: 2500
        //           });
        //           this.initdata()
        //           this.initdata2()
        //       }).catch(()=>{
        //           console.log("fdf")
        //       })
        //   }).catch(() => {
        //       this.$message({
        //           type: 'info',
        //           message: '已取消删除'
        //       });          
        //   });
      },


      handleEdit(index, val){
        this.isAdd = false
        const _this = this.$refs.scheduleForm
        _this.form = {
          id: val.id,
          project_id: val.project_id,
          start_time: val.start_time,
          end_time: val.end_time,
          sub_project_name: val.sub_project_name,
          sub_project_status: val.sub_project_status,

        }
        _this.dialog = true
      },
      handleDelete(index, val){
        // deleteParticipantsinfo(val.id).then( res => {
        //   this.$notify({
        //       title: '删除成功',
        //       type: 'success',
        //       duration: 2500
        //   })
        //   this.initdata()
        //   this.initdata2()
        // }).catch(err => {
        //     console.log("fdf")
        // })
      },


      handleSizeChange2(val) {
        this.page = 1
        this.size = val
        this.initdata2()
      },
      handleCurrentChange2(val) {
        this.page = val
        this.initdata2()
      },
    }
}
</script>
<style>
  .head-container {
    padding-bottom: 10px;
  }
  .filter-item {
    display: inline-block;
    vertical-align: middle;
    margin: 0 3px 10px 0;
  }
  .scheduleinfo {
    padding: 10px 25px;
  }

</style>