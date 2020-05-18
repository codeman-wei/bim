<template>
    <div class="users-info">

        <el-row style="margin:15px 10px;"> 
            <div style="float:left">
                <el-input v-model="keyword" clearable size="mini" placeholder="输入名称或者邮箱搜索" style="width: 200px;"  class="filter-item" @keyup.enter.native="search"/>
                <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="search">搜索</el-button>
                <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh" @click="reset">重置</el-button>

            </div>
            <div style="float:right">
                <el-button type="primary" icon="el-icon-plus" size="mini" @click="add">新增</el-button>
                <el-button type="success" icon="el-icon-edit" size="mini" @click="batchRESSET">重置</el-button>
                <el-button type="danger" icon="el-icon-delete" size="mini" @click="batchDELETE">删除</el-button>
                <el-button type="warning" icon="el-icon-download" size="mini">导出</el-button>
            </div>
        </el-row>


        <div class="users-table">
            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" align="center" header-align="center"> </el-table-column>
                <el-table-column prop="username" label="用户名" align="center" header-align="center"> </el-table-column>
                <el-table-column prop="loginname" label="登录账号" align="center" header-align="center"> </el-table-column>
                <el-table-column prop="telphone" label="联系电话" align="center" header-align="center"> </el-table-column>
                <el-table-column prop="userdetail" label="用户详情" align="center" header-align="center"> </el-table-column>
                <el-table-column prop="lastlogin" label="最后登录" align="center" header-align="center"> </el-table-column>
                <el-table-column label="操作" align="center" header-align="center">
                <template slot-scope="scope">
                    <el-button size="mini" @click="handleReset(scope.$index, scope.row)">重置</el-button>
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


        </div>
        <userform ref="userform" :isAdd= "isAdd" />
    </div>
</template>
<script>
import Userform from '@/views/userinformation/userform'
import { ResetPassword, showAllUser, DeleteUser } from '@/api/user/user'
import { deleteBatchUser, batchResetPassword} from '@/api/user/user'
export default {
    components: {
        "userform": Userform,
    },
    created(){
        this.initdata();
    },
    data() {
        return {
            total: 0,
            isAdd: true,
            size: 10,
            page: 1,
            keyword:'',
            tableData: [],
        }
    },
    methods: {
        initdata(){
            const sort = 'id,desc'
            let params = {
                page: this.page,
                size: this.size,
                sort: sort
            }
            if(this.keyword !== '') {
                params['blurry'] = this.keyword
            }
            showAllUser(params).then(res => { 
                this.total = res.data.totalElements
                this.tableData = res.data.content 
            })
        },
        add() {
            this.isAdd = true,
            this.$refs.userform.dialog = true
        },

        handleReset(index, row) {
            ResetPassword(row.id).then( res => {
                this.$notify({
                    title: '重置成功',
                    type: 'success',
                    duration: 2500
                })
                this.initdata()
            }).catch(err => {
                console.log("fdf")
                //console.log(err.response.data.message)
            })
        },
        handleDelete(index, row) {
            DeleteUser(row.id).then( res => {
                this.$notify({
                    title: '删除成功',
                    type: 'success',
                    duration: 2500
                })
                this.initdata()
            }).catch(err => {
                console.log("fdf")
                //console.log(err.response.data.message)
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

        batchRESSET() {
            this.$confirm('您确定要批量重置吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    var ids = this.multipleSelection.map(item => item.id).join()//获取所有选中行的id组成的字符串，以逗号分隔
                    let param = {
                        "ids": ids
                    }
                    batchResetPassword(param).then(res=> {
                        this.$message({
                            type: 'success',
                            message: '重置成功!',
                            duration: 2500
                        });
                    this.initdata()
                    }).catch(()=>{
                        console.log("fdf")
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消重置'
                    });          
                });
        },

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
                deleteBatchUser(param).then(res=> {
                    this.$message({
                        type: 'success',
                        message: '删除成功!',
                        duration: 2500
                    });
                    this.initdata()
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

        handleSelectionChange(val) {
            this.multipleSelection = val;
        },
        search() {
            this.page = 1
            this.initdata()
        },
        retset() {
            this.page = 1
            this.keyword = ""
            this.initdata()
        }
    }
}
</script>
<style>
    .users-info {
        padding: 10px 25px;
    }

    .users-table {
        margin-top: 20px;
    }

    .addForm {
        display: inline-block;
    }
</style>