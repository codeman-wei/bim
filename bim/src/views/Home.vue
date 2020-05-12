<template>
    <div style="height: 100%">
        <el-row>
            <my-header></my-header>
        </el-row>
        <el-row style="height: 100%">
            <el-col :span="4">
                <!-- <h5 class = "">首页</h5> -->
                <el-menu
                    :router=true 
                    :default-active="$route.name"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @close="handleClose"
                >
                <el-menu-item index="home">
                    <i class="el-icon-s-home"></i>
                    <span slot="title">首页</span>
                </el-menu-item>

                <el-submenu index="2">
                    <template slot="title">
                        <i class="el-icon-s-tools"></i>
                        <span>附属设施构件</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="2-1">整体模型</el-menu-item> 
                        <el-menu-item index="sub2">通航孔桥附属设施</el-menu-item>
                        <el-menu-item index="2-3">非通航孔桥结构附属设施</el-menu-item>
                        <el-menu-item index="2-4">全桥风屏障及声屏障</el-menu-item>
                        <el-menu-item index="2-5">桥梁综合接地设施</el-menu-item>
                        <el-menu-item index="2-6">桥梁供电、照明设施</el-menu-item>
                        <el-menu-item index="health">健康监测系统预留件</el-menu-item>
                        <el-menu-item index="2-8">修改记录</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index = "3">
                    <template slot="title">
                        <i class="el-icon-folder-opened"></i>
                        <span>附属设施文档</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="3-1">工程数量表</el-menu-item> 
                        <el-menu-item index="3-2">图纸文件</el-menu-item>
                        <el-menu-item index="3-3">模型文件</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index = "4">
                    <template slot="title">
                        <i class="el-icon-location"></i>
                        <span>施工动态</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="4-1">施工流程</el-menu-item> 
                        <el-menu-item index="4-2">施工进度管理</el-menu-item>
                        <el-menu-item index="4-3">参建人员信息</el-menu-item>
                        <el-menu-item index="4-4">个人工作平台</el-menu-item>
                        <el-menu-item index="4-5">安全质量管理</el-menu-item>
                        <el-menu-item index="4-6">动态决策管理</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index = "5">
                    <template slot="title">
                        <i class="el-icon-menu"></i>
                        <span>运维管控</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="5-1">工作人员信息</el-menu-item> 
                        <el-menu-item index="5-2">系统能耗管理</el-menu-item>
                        <el-menu-item index="5-3">系统健康监测</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-menu-item index="6">
                    <i class="el-icon-user-solid"></i>
                    <span slot="title">用户中心</span>
                </el-menu-item>
                <el-menu-item index="test">
                    <i class="el-icon-edit-outline" />
                    <span slot="title">测试</span>
                </el-menu-item>
            </el-menu>
            </el-col>
            <el-col :span="20" style="height: 100%">
                <!-- <div class='Imgroll' >
                    <el-carousel >
                        <el-carousel-item v-for="(item,index) in imgUrls" :key="index">
                            <img ref='img' :src="item.imageUrl" class="carousel_image_type"/>
                        </el-carousel-item>
                    </el-carousel>
                    <div class="content">
                        <span class="title">央视再聚焦！平潭海峡公铁两用大桥铁路铺轨进入最后阶段</span>
                        <div class="main">
                            <p>
                                平潭海峡公铁两用大桥啦！世界最长的跨海峡公铁两用大桥一一平潭海峡公铁两用大桥，
                                目前公路部分主体工程已经全部完工，铁路部分最后一座铁路桥正在架梁铺轨。
                                通车后，大桥作为京台高速的咽喉部分，将有力推进海峡两岸基础设施的联通。
                                这里是世界三大风暴海域之一，一年中6级以上大风天超过300天这里无风也起浪水流速度相当于长江中下游洪峰这里小岛棋布、
                                地质复杂坚硬如铁的光板岩石是打桩建墩者的噩梦.....
                            </p>
                        </div>
                    </div>
                </div> -->

                <router-view></router-view>
                <EditPassword ref="pass" />
                <UserInformation ref="userinfo" />
            </el-col>
        </el-row>
        
    </div>
</template>

<script>
import Header from '@/views/Header'
import EditPassword from '@/views/EditPassword'
import UserInformation from '@/views/UserInfo'
export default {
    components: {
        "my-header": Header,
        'EditPassword': EditPassword,
        'UserInformation':UserInformation
    },
    data() {
        return {
            imgUrls:[]
        };
    },
    mounted(){
      this.getImages();
    },
    methods: {
        handleOpen(key, keyPath) {
        console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
        console.log(key, keyPath);
        },
        goTo(path) {
        this.$router.replace(path);
        },
        getImages() {
            const data = [
                {
                    imageUrl: "./static/image/平潭大桥渲染图/2.jpg"
                },
                {
                    imageUrl: "./static/image/平潭大桥渲染图/3.jpg"
                },
            ]

            this.imgUrls = data
        },

        // 数据请求服务，一般是返回的一个promise对象，  是一个异步处理的解决方案，
        getImgUrl(){

        },


    }
};
</script>

<style scoped>
    .el-col-12{
        width: 16%;
    }
    .Imgroll{
        padding: 20px ;

    }
    .carousel_image_type {
        width: 100%;
        height: 100%;
    }
    .content {
        margin-top: 10px;
        font-family: Arial, Helvetica, sans-serif;
        
    }
    .title {
        display: block;
        font-size: 1.57em;
        margin-block-start: 1em;
        margin-block-end: 1em;
        margin-inline-start: 0px;
        margin-inline-end: 0px;
        font-weight: bold;
    }
    .main {
        text-indent: 2em;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 5px;
        
    }
</style>