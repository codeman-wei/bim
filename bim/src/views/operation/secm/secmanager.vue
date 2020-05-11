<template>
  <div class="app-container">
    <div class="head-container">
        <div>
          <el-input
              v-model="blurry"
              clearable
              size="small"
              placeholder="输入名称或者邮箱搜索"
              style="width: 200px;"
              class="filter-item"
              @keyup.enter.native="search"
          />
          <span>
            <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="search">搜索</el-button>
            <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh-left" @click="handleReset">重置</el-button>
          </span>
          <div style="float:right">
              <el-button
                class="filter-item"
                type="primary"
                icon="el-icon-plus"
                size="mini"
                @click="handleAdd">
                新增
              </el-button>
              <el-button 
                class="filter-item"
                size="mini"
                type="success"
                icon="el-icon-edit"
                :disabled="multipleSelection.length !== 1"
                @click="handleEdit(multipleSelection[0])"
              >
                修改
              </el-button>
              <el-button
                class="filter-item"
                type="danger"
                icon="el-icon-delete"
                size="mini"
                :disabled="multipleSelection.length === 0"
                @click="handleDelete(multipleSelection, true)">
                删除
              </el-button>
              <el-button class="filter-item" type="warning" icon="el-icon-download" size="mini">导出</el-button>
          </div>
        </div>
    </div>
    <!--表单渲染-->
    <el-dialog append-to-body :close-on-click-modal="false" :before-close="cancelCU" :visible.sync="diagVisable" :title="cuStatus === 0 ? '添加':'编辑'" width="580px" @open="getProjectData">
      <el-form ref="form" :inline="true"  :model="form" :rules="rules" size="small" label-width="76px">
        <el-form-item label="设备名称" prop="username">
          <el-input v-model="form.device_name" />
        </el-form-item>
        <el-form-item label="数量" prop="number">
          <el-input v-model.number="form.number" />
        </el-form-item>
        <el-form-item label="规格" prop="specification">
          <el-input v-model="form.specification" />
        </el-form-item>
        <el-form-item label="施工专项">
          <el-select v-model="form.project_id" placeholder="请选择" style="width: 187px">
            <el-option
              v-for="item in projectData"
              :key="item.id"
              :label="item.item_name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="text" @click="cancelCU">取消</el-button>
        <el-button type="primary" @click="submitCU">确认</el-button>
      </div>
    </el-dialog>
    <div class="table-container">
        <el-table ref="multipleTable" size="medium" :data="tableData" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55" />
            <el-table-column prop="device_name" label="设备名称" align="center" />
            <el-table-column prop="specification" label="规格" align="center" />
            <el-table-column prop="number" label="数量" align="center" />
            <el-table-column prop="project.item_name" label="所属施工专项" align="center" />
            <el-table-column label="操作" align="center">
            <template slot-scope="scope">
                <el-button size="mini" icon="el-icon-edit" type="primary" @click="handleEdit(scope.row)" />
                <el-button size="mini" type="danger" icon="el-icon-delete" style="margin-left: 0px" @click="handleDelete(scope.row.id)" />
                <!-- <el-popover v-model="pop" v-permission="permission.del" placement="top" width="180" trigger="manual" @show="onPopoverShow" @hide="onPopoverHide">
                  <p>确定删除本条数据吗？</p>
                  <div style="text-align: right; margin: 0">
                    <el-button size="mini" type="text" @click="pop=false">取消</el-button>
                    <el-button type="primary" size="mini" @click="handleDelete(scope.row.id)">确定</el-button>
                  </div>
                  <el-button slot="reference" type="danger" icon="el-icon-delete" size="mini" @click="pop = true" />
                </el-popover> -->
            </template>
            </el-table-column>
        </el-table>
        
        <div class="block">
          <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            style="margin-top: 8px;"
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
import { getAll, add, edit, del } from '@/api/operation/secmanager'
import { getProjectList } from '@/api/schedule/subproject'
export default {
  name: "Secmanager",
  created(){
        this.initData();
    },
    data() {
      return {
        total: 0, isAdd: true, size: 10, page: 1, blurry:'', pop: false,
        multipleSelection: [], tableData: [], projectData: [], cuStatus: 0, diagVisable: false,
        form: { id: '', device_name: null, specification: null, number: null, project_id: null },
        rules: {

        }
      }
    },
    methods: {
      initData(){
        let params = {
            page: this.page,
            size: this.size,
        }
        if(this.blurry !== '') {
            params['blurry'] = this.blurry
        }
        getAll(params).then(res => { 
            this.total = res.data.totalElements
            this.tableData = res.data.content 
        })
      },
      getProjectData() {
        getProjectList().then(res => {
          this.projectData = res.data
        })
      },
      search() {
        this.page = 1
        this.initData()
      },
      cancelCU(){
        this.form = { id: '', device_name: null, specification: null, number: null, project_id: null }
        this.diagVisable = false
      },
      submitCU(){
        if (this.cuStatus === 0) {
          add(this.form).then(res => {
            this.$notify({
              title: '添加成功',
              type: 'success',
              duration: 2500
            })
            this.form = { id: '', device_name: null, specification: null, number: null, project_id: null }
            this.initData()
            this.diagVisable = false
          })
        } else {
          edit(this.form).then(res => {
            this.$notify({
              title: '编辑成功',
              type: 'success',
              duration: 2500
            })
            this.form = { id: '', device_name: null, specification: null, number: null, project_id: null }
            this.initData()
            this.diagVisable = false
          })
        }
      },
      handleEdit(val) {
        this.cuStatus = 1
        for (const key in this.form) {
          if (val.hasOwnProperty(key)) {
            this.form[key] = val[key]
          }
        }
        this.diagVisable = true
      },
      handleAdd() {
        // this.getProjectData()
        this.cuStatus = 0
        this.diagVisable = true
      },
      handleDelete(val, multi=false) {
        let ids = ''
        let mes = ''
        if (multi) {
          ids = val.map(item => item.id).join()
          mes = '您确定要批量删除吗?'
        } else {
          ids = val.toString()
          mes = '您确定要删除本条信息吗?'
        }
        this.$confirm( mes, '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          const param = {
            "ids": ids
          }
          del(param).then(res => {
            this.$notify({
              title: '删除成功',
              type: 'success',
              duration: 2500
            })
            this.initData()
          }).catch(() => {
          })
        })
      },
      handleReset(index, val) {
        this.blurry = '',
        this.page = 1,
        this.initData()
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
      handleSelectionChange(val) {
        this.multipleSelection = val
      },
      doCancel() {
        this.pop = false
      }
    }
}
</script>
<style lang="scss">
</style>