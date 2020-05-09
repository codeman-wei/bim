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
        <ManagerForm ref="managerform" :isAdd= "isAdd" />
    </el-dialog>
    
</template>
<script>
import { parseTime } from '@/utils/index'
import { getSubprojectById } from '@/api/schedule/subproject'
import ManagerForm from '@/views/schedule/managerform'
import echarts from 'echarts'
export default {
    components: {
        "ManagerForm": ManagerForm,
    },
    props: {
      title: {
        type: String,
        required: true
      },
    },
    data() {
        return{
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
            isAdd: true
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
        cancel(){
            this.dialog = false
        },
        handleClick() {

        },
        handleSelectionChange() {

        },
        handleDelete(){},
        handleupdate(){},
        initdata(id){
            getSubprojectById(id).then(res => {
                console.log(res)
                this.tableData = res.data
            })

        },
        batchDelete(){},
        add(){
            console.log(this.$refs)
            this.isAdd = true,
            this.$refs.managerform.dialog = true

        },
    }
}
</script>
<style>

</style>