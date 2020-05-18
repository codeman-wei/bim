<template>
    <div class="sysmonitor-info">
        <el-row style="margin-bottom:20px;"> 
            <div style="float:left">
                <el-date-picker v-model="time" type="date" placeholder="选择日期" size='mini' value-format = 'yyyy-MM-dd'></el-date-picker>
                <el-button class="filter-item" size="mini" type="success" icon="el-icon-search" @click="search">搜索</el-button>
                <el-button class="filter-item" size="mini" type="warning" icon="el-icon-refresh" @click="reset">重置</el-button>
            </div>
            <div style="float:right">
                <el-button class="filter-item" type="primary" icon="el-icon-plus" size="mini" @click="add">新增</el-button>
                <el-button class="filter-item" type="danger" icon="el-icon-delete" size="mini" disabled>删除</el-button>
                <el-button class="filter-item" type="success" icon="el-icon-upload" size="mini" disabled>导入</el-button>
                <el-button class="filter-item" type="warning" icon="el-icon-download" size="mini" disabled>导出</el-button>
            </div>
        </el-row>
        <el-row :gutter= "15">
            <el-col :xs="24" :sm="24" :md="10" :lg="10" :xl="10" style="margin-bottom: 10px">
                <el-card class="box-card" shadow="never">
                    <div slot="header" class="clearfix">
                        <span class="sys-span">系统健康监测</span>
                    </div>
                    <el-table ref="table" v-loading="loading" highlight-current-row style="width: 100%;" :data="tableData" 
                        @current-change="handleCurrentChange">
                        <el-table-column prop="sectionsname" label="区段" width="120" align="left" header-align="center"> </el-table-column>
                        <el-table-column prop="stresses" label="应力" width="120" align="center" header-align="center"> </el-table-column>
                        <el-table-column prop="shape" label="变形" width="120" align="center" header-align="center"> </el-table-column>
                        <el-table-column prop="temperature" label="温度" width="120" align="center" header-align="center"> </el-table-column>
                        <el-table-column prop="humidity" label="湿度" width="120" align="center" header-align="center"> </el-table-column>
                        <el-table-column prop="windpower" label="风力" width="120" align="center" header-align="center"> </el-table-column>
                    </el-table>
                </el-card>
            </el-col>
                <!-- 菜单授权 -->
            <el-col :xs="24" :sm="24" :md="14" :lg="14" :xl="14">
                <el-card class="box-card" shadow="never">
                        <div slot="header" class="clearfix">
                            <el-tooltip class="item" effect="dark" content="选择指定角色分配菜单" placement="top">
                            <span class="sys-span">每周详情</span>
                        </el-tooltip>
                        </div>
                        <div id="orderStatistics" style="width:100%; height:400px; "></div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>
<script>
import echarts from 'echarts'
export default {

    data() {
        return {
            charts: '',
            loading: false,
            time: '',
            page: 1,
            tableData: [
                {sectionsname: '一区段', stresses: '32', shape: '35', temperature: '53', humidity: '22',windpower: '12'},
                {sectionsname: '二区段', stresses: '45', shape: '', temperature: '', humidity: '',windpower: ''},
                {sectionsname: '三区段', stresses: '75', shape: '', temperature: '', humidity: '',windpower: ''},
                {sectionsname: '四区段', stresses: '32', shape: '', temperature: '', humidity: '',windpower: ''},
                {sectionsname: '元洪航道段', stresses: '11', shape: '', temperature: '', humidity: '',windpower: ''},
            ],
            opinionData: ["3", "2", "4", "4", "5"],
        }
    },

    methods: {
        search() {
            console.log(this.time)
        },
        add() {},
        upload() {},
        reset(){},

        handleSizeChange() {},
        handleCurrentChange(val) {
            // console.log(val)
            this.getLine()
        },
        handleSelectionChange() {},
        // 折线图
        getLine () {
            console.log('tek')
            // 基于准备好的dom，初始化echarts实例
            this.charts = echarts.init(document.getElementById('orderStatistics'));
            // 绘制图表，this.echarts1_option是数据
            this.charts.setOption({
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['近七日变化']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },

                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                data: ["1","2","3","4","5","6","7"]
                
                },
                yAxis: {
                    type: 'value'
                },

                series: [{
                    name: '近七日变化',
                    type: 'line',
                    stack: '总量',
                    data: this.opinionData
                }]
            })

            console.log(this.charts)
        },
    }
}
</script>
<style>
    .sysmonitor-info {
        padding: 10px 25px;
    }
    .sysmonitor-table {
        margin-top: 20px;
    }

    .sys-span {
        font-weight: bold;color: #303133;
        font-size: 15px;
    }
    .head-container {
        padding-bottom: 10px;
    }
    .filter-item {
        display: inline-block;
        vertical-align: middle;
        /* margin: 0 0px 10px 0; */
    }
</style>