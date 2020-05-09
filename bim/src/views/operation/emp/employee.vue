<template>
    <div class="emp-info">
        <div class="emp-button" >
            <div style="float:left">
                <el-input v-model="keyword" 
                    clearable size="small" 
                    placeholder="输入员工姓名"
                    style="width: 200px;"
                    class="filter-item"
                />
            <el-button type="primary" icon="el-icon-search" size="small" @click="search">搜索</el-button>
            <el-button type="success" icon="el-icon-search" size="small" @click="resetKeyword">重置</el-button>
            </div>
            <div style="float:right">
                <el-button type="primary" icon="el-icon-plus" size="small" @click="add">新增</el-button>
                <el-button type="danger" icon="el-icon-delete" size="small" @click="batchDelete" :disabled="this.tableData.length === 0">删除</el-button>
                <el-button type="success" icon="el-icon-upload" size="small" @click="upload">导入</el-button>
                <el-button type="warning" icon="el-icon-download" size="small">导出</el-button>
            </div>
        </div>
        <div class="emp-table">
            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange" @current-change="handleCurrentChange">
                <el-table-column type="selection" width="55"> </el-table-column>
                <el-table-column prop="employee_name" label="员工姓名" width="100"> </el-table-column>
                <el-table-column prop="employee_number" label="员工工号" width="100"> </el-table-column>
                <el-table-column prop="employee_tel" label="员工电话" width="120"> </el-table-column>
                <el-table-column prop="employee_id_number" label="岗位证号" width="150"> </el-table-column>
                <el-table-column prop="employee_dept" label="部门" width="80"></el-table-column>
                <el-table-column prop="employee_project" label="所属施工专项"></el-table-column>
                <el-table-column prop="employee_job" label="负责内容"> </el-table-column>
                <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
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
            <empform ref="empform" :isAdd="isAdd"/>
            <empupload ref="empupload" />
        </div>
    </div>

    
</template>
<script>
import { getAllEmp, deleteEmp, deleteBatchEmp } from '@/api/operation/employee'
import Empform from '@/views/operation/emp/empform'
import EmpUpload from '@/views/operation/emp/empupload'
export default {
    components: {
        "empform": Empform,
        "empupload": EmpUpload
    },
    created() {
        this.initData();
    },
    data() {
        return {
            total: 0,
            size: 10,
            keyword: '',
            tableData: [],
            page: 1,
            isAdd:true,
            multipleSelection : []
        }
    },
    methods: {
        resetKeyword() {
            this.keyword = '',
            this.page = 1,
            this.initData()
        },
        search() {
            this.page = 1,
            this.initData()
        },
        add() {
            this.isAdd = true,
            this.$refs.empform.dialog = true
        },
        upload() {
            this.$refs.empupload.dialog = true
        },
        initData(){
            const sort = 'id,desc'
            let params = {
                page: this.page,
                size: this.size,
                sort: sort
            }
            if(this.keyword !== '') {
                params['employee_name'] = this.keyword
            }
            getAllEmp(params).then(res => {
                this.total = res.data.totalElements // 初始化时数据的总数
                this.tableData = res.data.content // 获取到的数据
            })
        },
        handleSelectionChange(val) {
            this.multipleSelection = val
        },

        handleEdit(index, row) {
            this.isAdd = false
            const _this = this.$refs.empform
            _this.form = {
                id: row.id,
                employee_name:  row.employee_name,
                employee_id_number: row.employee_id_number,
                employee_job:  row.employee_job,
                employee_number:  row.employee_number,
                employee_project:  row.employee_project,
                employee_tel:  row.employee_tel,
                employee_dept: row.employee_dept,
           }
           _this.dialog = true
        },
        handleDelete(index, row) {
            deleteEmp(row.id).then( res => {
                this.$notify({
                    title: '删除成功',
                    type: 'success',
                    duration: 2500
                })
                this.initData()
            }).catch(err => {
                console.log("fdf")
            })
        },
        handleSizeChange(val) {
            this.page = 0
            this.size = val
            this.initData()
        },
        handleCurrentChange(val) {
            this.page = val
            this.initData()
        },
        batchDelete() {
            this.$confirm('您确定要批量删除吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                var ids = this.multipleSelection.map(item => item.id).join()//获取所有选中行的id组成的字符串，以逗号分隔
                let param = {
                    "ids": ids
                }
                deleteBatchEmp(param).then(res=> {
                    this.$message({
                        type: 'success',
                        message: '删除成功!',
                        duration: 2500
                    });
                    this.initData()
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
    }
}
</script>
<style>
    .emp-info {
        padding: 10px 25px;
    }

    .emp-table {
        margin-top: 50px;
    }
</style>