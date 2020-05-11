<template>
    <div class="schedule-info" >
        <!-- <div class="schedule-button">
            <div style="float:left">
                <el-input
                    v-model="keyword"
                    clearable
                    size="small"
                    placeholder="输入名称或者邮箱搜索"
                    style="width: 200px;"
                    class="filter-item"
                    @keyup.enter.native="search"
                />
                <el-button type="primary" icon="el-icon-search" size="small">搜索</el-button>
            </div>
            <div style="float:right">
                <el-button type="primary" icon="el-icon-plus" size="small" @click="add">新增</el-button>
                <el-button type="success" icon="el-icon-edit" size="small" @click="batchRESSET">重置</el-button>
                <el-button type="danger" icon="el-icon-delete" size="small" @click="batchDELETE">删除</el-button>
                <el-button type="warning" icon="el-icon-download" size="small">导出</el-button>
            </div>
        </div> -->

        <el-row class="tab-actions" v-for="(tabs, index) in tablists" :key= index>
            <el-col :lg="8" class="tab-action-item" v-for="(tab,index) in tabs" :key= index>
                <!-- <el-card :body-style="{ padding: '0px' }"> -->
                <div class="block">
                    <img :src= "imageApi + '/bridge_img/' + tab.item_img_href" class="image" @click="show(tab)">
                    <div style="padding: 14px;">
                        <span>{{tab.item_name}}</span>
                        <!-- <div class="bottom clearfix">
                            <time class="time">{{ currentDate }}</time>
                            <el-button type="text" class="button">操作按钮</el-button>
                        </div> -->
                    </div>
                <!-- </el-card> -->
                </div>
            </el-col>
        </el-row>
        <ManagerCard ref="managercard" :title= "title" />
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
import ManagerCard from '@/views/schedule/managercard'
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
            title:'',
            key: '',
            key2: '',
            tablists: [],
        }
    },
    methods: {

        initdata(){
            showAllProject().then(res => {
                this.tablists = res.data
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
      margin: 10px 10px;
  }
</style>