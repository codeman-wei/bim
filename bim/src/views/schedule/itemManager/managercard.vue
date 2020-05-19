<template>
  <el-dialog :visible.sync="dialog" :close-on-click-modal="false" :before-close="cancel" :title="title" append-to-body 
    width="1000px" @close="cancel">
    <el-tabs type="border-card">
      <el-tab-pane label="施工进度">
        <div class="card-bn" style="float:right; margin-button:2px;">
          <el-button type="primary" icon="el-icon-plus" size="mini" @click="add">新增</el-button>
          <el-button type="danger" icon="el-icon-delete" size="mini" @click="batchDelete" :disabled="this.tableData.length === 0">删除</el-button>
        </div>
        <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
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
          <el-table-column prop="sub_project_status" label="当前状态" > </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
                <el-button size="mini" @click="handleupdate(scope.$index, scope.row)">修改</el-button>
                <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
        </el-tab-pane>
        <el-tab-pane label="施工流程">
            <!-- <div style="float:right; width:100%; height:100px;" id="legend" ></div> -->
            <div class="height: 100px">
                <el-timeline :reverse="reverse">
                    <el-timeline-item
                        v-for="(activity, index) in tableData"
                        :key="index"
                        :color="activity.sub_project_status === '已完成'?'#0bbd87' : '#FF0000'" 
                        :timestamp="parseTime(activity.start_time)">
                        {{activity.sub_project_name}}
                    </el-timeline-item>
                </el-timeline>
            </div>
        </el-tab-pane>
    </el-tabs>
    <!-- <ManagerForm ref="managerform" :isAdd= "isAdd" /> -->
  </el-dialog>
</template>
<script>
import { parseTime } from '@/utils/index'
// import { getSubprojectById } from '@/api/schedule/subproject'
// import ManagerForm from '@/views/schedule/itemManager/managerform'
import echarts from 'echarts'
export default {
    // components: {
    //     "ManagerForm": ManagerForm,
    // },
    props: {
      isAdd: {
        type: Boolean,
        required: true
      },
    },
    data() {
        return{
            page: 1,
            size: 10,
            total: 0,

            reverse: false,
            dialog: false,
            tableData: [],
            legend: {
                data: ["已完成", "未完成"],
                icon: "circle",   //  这个字段控制形状  类型包括 circle，rect ，roundRect，triangle，diamond，pin，arrow，none
                itemWidth: 10,  // 设置宽度
                itemHeight: 10, // 设置高度
                itemGap: 40 // 设置间距

            },
            isAdd: true,
            multipleSelection: []
        } 
    },

    methods: {
        parseTime,
        getlegend() {
            this.charts = echarts.init(document.getElementById('legend'));
            this.charts.setOption({
                legend: {
                    data: this.legend
                },
            })
        },
        handleSizeChange(val) {
            this.page = 1
            this.size = val
            // this.initdata()
        },
        handleCurrentChange() {
            this.page = val
            // this.initdata()
        },
        cancel(){
            this.dialog = false
        },
        handleSelectionChange(val){
            this.multipleSelection = val
        },
        handleDelete(index, val){},
        handleupdate(index, val){
            this.isAdd = false
            const _this = this.$refs.managerform
            _this.form = {
                id: val.id,
                sub_project_name: val.sub_project_name,
                start_time: val.start_time,
                end_time: val.end_time,
                sub_project_status: val.sub_project_status
            }
            _this.dialog = true
        },
        initdata(id){
            getSubprojectById(id).then(res => {
                this.tableData = res.data
            })
        },
        batchDelete(){},
        add(){
            this.isAdd = true,
            this.$refs.managerform.form.sub_project_status = 1
            this.$refs.managerform.dialog = true

        },
    }
}
</script>
<style>

</style>