<template>
  <div class="participantsinfo">
    <el-row :gutter= "15">
      <el-col :xs="24" :sm="24" :md="9" :lg="9" :xl="9" >
          <el-card class="box-card" shadow="never">
              <div slot="header" class="clearfix">
                <span class="sys-span">施工项目列表</span>
              </div>
              <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%">
                  <el-table-column prop="item_name" label="施工项目" width="160"> </el-table-column>
                  <el-table-column prop="item_total" label="参建人数" width="80"> </el-table-column>
                  <el-table-column label="操作" >
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
      <el-col :xs="24" :sm="24" :md="15" :lg="15" :xl="15">
        <el-card class="box-card" v-if="selectedProjectID === false">
          <div slot="header" class="clearfix">
            <span class="sys-span">参建人员信息</span>
          </div>
          <div class="head-container">
            请选择施工项目
          </div>
        </el-card>
        <el-card class="box-card" shadow="never" v-if="selectedProjectID === true">
          <div slot="header" class="clearfix">
            <span>参建人员信息</span>
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
            <div style="float:left;">
              <!-- 新增 -->
              <el-button class="filter-item" size="mini" type="primary" icon="el-icon-plus" @click="add" >新增</el-button>
              <!-- 导出 -->
              <el-button class="filter-item" size="mini" type="warning" icon="el-icon-download" @click="download" :disabled="this.tableData2.length === 0">导出</el-button>
              <!-- 导入 -->                  
              <el-button class="filter-item" size="mini" type="success" icon="el-icon-upload"  @click="upload" :disabled="this.tableData2.length === 0">导入</el-button>
              <!-- 删除 -->
              <el-button class="filter-item" size="mini" type="danger" icon="el-icon-delete"  @click="batchDELETE" :disabled="this.tableData2.length === 0">删除</el-button>
            </div>
        
            <el-table ref="multipleTable2" :data="tableData2" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange2">
                <el-table-column type="selection" width="55"> </el-table-column>
                <el-table-column prop="participants_name" label="姓名" width="55"> </el-table-column>
                <el-table-column label="性别" width="55"> 
                  <template slot-scope="scope">
                    {{ scope.row.participants_sex === 1 ? '男' : '女' }}
                  </template>
                </el-table-column>
                <el-table-column prop="participants_tel" label="联系方式" width='120'> </el-table-column>
                <el-table-column prop="participants_qualification" label="从业资格" width="100"> </el-table-column>
                <el-table-column label="岗位状态" width="100"> 
                  <template slot-scope="scope">
                    {{ scope.row.participants_work_status === 1 ? '在岗' : '离岗' }}
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
    <participantform ref="participantform" :isAdd=isAdd />
  </div>
</template>
<script>
import {getParticipantsInfo, getParticipantsInfoByPID, deleteParticipantsinfo } from "@/api/schedule/paticipantsinfo"
import participantform from '@/views/schedule/participantsinfo/participantsform'
import {deleteBatchParticipantsinfo} from "@/api/schedule/paticipantsinfo"
export default {
    components: {
        "participantform": participantform,
    },
    data(){
      return {
        selectedProjectID: false,
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
      initdata() {
        const sort = 'id,desc'
        let params = {
          page: this.page,
          size: this.size,
          sort: sort
        }
        getParticipantsInfo(params).then(res => {
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
        this.selectedProjectID = true
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
          params['participants_name'] = this.keyword
        }
        getParticipantsInfoByPID(params).then(res => {
          this.tableData2 = res.data.content
          this.total2 = res.data.totalElements
        })
      },
      handleSelectionChange2(val){
        this.multipleSelection = val
      },
      handleEdit(index, val){
        this.isAdd = false
        const _this = this.$refs.participantform
        _this.form = {
          id: val.id,
          project_id: val.project_id,
          participants_name: val.participants_name,
          participants_sex: val.participants_sex,
          participants_tel: val.participants_tel,
          participants_work_status: val.participants_work_status,
          participants_qualification: val.participants_qualification
        }
        _this.dialog = true
      },
      handleDelete(index, val){
        deleteParticipantsinfo(val.id).then( res => {
          this.$notify({
              title: '删除成功',
              type: 'success',
              duration: 2500
          })
          this.initdata()
          this.initdata2()
        }).catch(err => {
            console.log("fdf")
        })
      },
      add() {
        this.isAdd = true
        this.$refs.participantform.dialog = true
      },
      upload() {},
      download() {},
      batchDELETE() {
        this.$confirm('您确定要批量删除吗?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
          }).then(() => {
              var ids = this.multipleSelection.map(item => item.id).join()//获取所有选中行的id组成的字符串，以逗号分隔
              let param = {
                  "ids": ids
              }
              deleteBatchParticipantsinfo(param).then(res=> {
                  this.$message({
                      type: 'success',
                      message: '删除成功!',
                      duration: 2500
                  });
                  this.initdata()
                  this.initdata2()
              }).catch(()=>{
                  console.log("fdf")
              })
          }).catch(() => {
              this.$message({
                  type: 'info',
                  message: '已取消删除'
              });          
          });
      },
      reset(){
        this.keyword =""
        this.initdata2()
      },
      search() {
        this.page = 1,
        this.initdata2()
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
  .participantsinfo {
    padding: 10px 25px;
  }

</style>