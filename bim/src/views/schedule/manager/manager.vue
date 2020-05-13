<template>
    <div class="schedule-info" >
        <el-row style="margin:15px 10px;"> 
            <div style="float:left">
                <el-input v-model="keyword" clearable size="small" placeholder="请输入项目名称" style="width: 200px;"
                    class="filter-item" @keyup.enter.native="search" />
                <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="search">搜索</el-button>
                <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh" @click="reset">重置</el-button>

            </div>
            <div style="float:right">
                <el-button type="primary" icon="el-icon-plus" size="small" @click="add">新增</el-button>
                <el-button type="danger" icon="el-icon-delete" size="small" @click="batchDELETE">删除</el-button>
            </div>
        </el-row>

        <el-row class="tab-actions" v-for="(tabs, index) in tablists" :key= index>
            <el-col :lg="6" class="tab-action-item" v-for="(tab,index) in tabs" :key= index>
                <div class="block">
                    <img :src= "imageApi + '/bridge_img/' + tab.item_img_href" class="image" @click="show(tab)">
                    <div class="content"> 
                        <span>{{tab.item_name | ellipsis}}</span>
                    </div>
                </div>
            </el-col>
        </el-row>

        <div class="block">
        <el-pagination
            @current-change="handleCurrentChange"
            :current-page.sync="page"
            :page-size="12"
            layout="prev, pager, next, jumper"
            :total= total>
        </el-pagination>
        </div>
        <ManagerCard ref="managercard" :title= "title" />
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
import ManagerCard from '@/views/schedule/manager/managercard'
import { showAllProject } from '@/api/schedule/schedule'
export default {
    components: {
        "ManagerCard": ManagerCard,
    },
    computed: {
    ...mapGetters([
        'baseApi',
        'imageApi'
      ])
    },
    created() {
        this.initdata()
    },
    data(){
        return {
            keyword: '',
            title:'',
            key: '',
            key2: '',
            tablists: [],
            total: 50,
            page: 1,
            size: 12,
        }
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
    methods: {
        search() {
            this.page = 1
            this.initdata()
        },
        add() {},
        reset() {
            this.keyword = ''
            this.initdata()
        },
        batchDELETE() {},
        handleSizeChange(val) {
            console.log(val)
        },
        handleCurrentChange(val) {
            console.log(val)
        },
        initdata(){
            const sort = 'id,desc'
            let params = {
                page: this.page,
                size: this.size,
                sort: sort
            }
            if(this.keyword !== ''){
                params['imageName'] = this.keyword
            }
            showAllProject(params).then(res => {
                let { content, totalElements } = res.data
                this.tablists = content
                this.total = totalElements
            })
        },
        show(val) {
            console.log(this.$refs)
            this.$refs.managercard.dialog = true
            this.title = val.item_name
            this.$refs.managercard.initdata(val.id)
            //this.$refs.manangercard.getlegend()
        }
    }
}
</script>
<style>
  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .block {
      margin: 20px 10px;
  }

  .content {
      margin-top: 5px;
      text-align: center;
      font-weight: bold;
      font-size: 15px;
      font-family: Arial, Helvetica, sans-serif;
  }
</style>