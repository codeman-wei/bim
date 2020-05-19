<template>
  <div class="app-container">
    <div class="head-container">
      <!-- 搜索框 -->
      <el-input
          v-model="query.blurry"
          clearable
          size="small"
          placeholder="输入名称或者邮箱搜索"
          style="width: 200px;"
          class="filter-item"
          @keyup.enter.native="toQuery"
      />
      <span>
        <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="toQuery">搜索</el-button>
        <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh-left" @click="handleReset">重置</el-button>
      </span>
      <!-- crud按钮 -->
      <div style="float:right">
        <el-button
          class="filter-item"
          type="primary"
          icon="el-icon-plus"
          size="mini"
          @click="showAddFormDialog">
          新增
        </el-button>
        <el-button 
          class="filter-item"
          size="mini"
          type="success"
          icon="el-icon-edit"
          :disabled="selections.length !== 1"
          @click="handleEdit(selections[0])">
          修改
        </el-button>
        <el-button
          class="filter-item"
          :loading="delAllLoading"
          type="danger"
          icon="el-icon-delete"
          size="mini"
          :disabled="selections.length === 0"
          @click="delAllMethod">
          删除
        </el-button>
        <el-button class="filter-item" type="warning" icon="el-icon-download" size="mini">导出</el-button>
      </div>
    </div>
    <!--表单渲染-->
    <el-dialog append-to-body :close-on-click-modal="false" :before-close="cancel" :visible.sync="dialog" :title="getFormTitle()" width="620px">
      <el-form ref="form" :inline="true"  :model="form"  size="small" label-width="76px">
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
        <el-button type="text" size="mini" @click="cancel">取消</el-button>
        <el-button type="primary" size="mini" @click="submitMethod">确认</el-button>
      </div>
    </el-dialog>
    <div class="table-container">
      <el-table ref="table" v-loading="loading" size="medium" :data="data" tooltip-effect="dark" style="width: 100%" @selection-change="handleSelectionChange">
        <el-table-column type="selection" width="55" />
        <el-table-column prop="device_name" label="设备名称" align="center" />
        <el-table-column prop="specification" label="规格" align="center" />
        <el-table-column prop="number" label="数量" align="center" />
        <el-table-column prop="project.item_name" label="所属施工专项" align="center" />
        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button size="mini" icon="el-icon-edit" type="primary" @click="handleEdit(scope.row)" />
            <el-popover :ref="scope.row.id" placement="top" width="180" trigger="click">
              <p style="margin: 10px 0">确定删除本条数据吗？</p>
              <div style="text-align: right; margin: 0">
                <el-button size="mini" type="text" @click="closePopover(scope.row.id)">取消</el-button>
                <el-button type="primary" :loading="delLoading" size="mini" @click="delMethod(scope.row.id)">确定</el-button>
              </div>
              <el-button slot="reference" type="danger" icon="el-icon-delete" size="mini"/>
            </el-popover>
          </template>
        </el-table-column>
      </el-table>
      <!-- 页码 -->
      <div class="block">
        <el-pagination
          @size-change="sizeChange"
          @current-change="pageChange"
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
import crudMethod from '@/api/operation/secmanager'
import { getProjectList } from '@/api/operation/secmanager'
import crud from '@/mixins/crud'
export default {
  name: "Secmanager",
  mixins: [ crud ],
  created(){
    this.init();
    this.crudMethod = crudMethod
    this.form = { id: '', device_name: null, specification: null, number: null, project_id: null }
    this.resetForm = { id: '', device_name: null, specification: null, number: null, project_id: null }
    // 提前获取项目列表
    this.getProjectData()
  },
  data() {
    return {
      projectData: [],
    }
  },
  methods: {
    beforeInit() {
      this.url = '/secmanager/'
      return true
    },
    getProjectData() {
      getProjectList().then(res => {
        this.projectData = res.data
      })
    },
  }
}
</script>
<style lang="scss">
</style>