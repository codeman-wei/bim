<template>
    <div class="topbar-wrap">

        <div class="topbar-title topbar-btn">
            <span>平潭海峡公铁两用大桥附属设施运维管控系统</span>
        </div>
        <div class="topbar-account topbar-btn">
            <el-dropdown trigger="click">
                <span class="el-dropdown-link userinfo-inner">
                    <i class="el-icon-user"></i> {{sysUserName}}  <i class="el-icon-menu"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item @click.native="userinfo">个人信息</el-dropdown-item>
                    <el-dropdown-item @click.native="editpwd">修改密码</el-dropdown-item>
                    <el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </div>
</template>
<script>



export default {

    data() {
        return {
            sysUserName: '',
            sysUserAvatar: '',
            collapsed: false,
        }
    },

    mounted() {
        var token = sessionStorage.getItem("token");
        var user = sessionStorage.getItem("name");
        if (token && user) {
            user = JSON.parse(user);
            this.sysUserName = user || "";
        } else {
            sessionStorage.removeItem("token");
            sessionStorage.removeItem("name");
            this.$router.push("/login");
        }
    },
    methods: {
        //用户信息
        userinfo() {
            this.$parent.$parent.$refs.userinfo.dialog = true
        },
        //修改密码
        editpwd() {
            this.$parent.$parent.$refs.pass.dialog = true
        },
        //退出
        logout() {     
            this.$confirm('确定退出系统, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.$store.dispatch('LogOut').then(()=>{
                    this.$message({
                        type: 'success',
                        message: '退出成功!'
                    });
                    sessionStorage.removeItem("token");
                    sessionStorage.removeItem("name");
                    this.$router.push({ path: '/' })
                })
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消退出'
                 });  
            
            });
        },
    }
  }
</script>
<style>
    .topbar-wrap{padding:0;height:50px;background:#1d8ce0;line-height:50px}
    .topbar-btn{color:#fff}
    .topbar-btn:hover{background-color:#58b7ff}
    .topbar-logo{width:49px;line-height:26px}
    .topbar-logo,.topbar-title{float:left;border-right:1px solid #1d8ce0;text-align:center}
    .topbar-title{width:400px;font-weight: bold;}
    .topbar-account{float:right;padding-right:9pt;font-size:9pt;font-weight: bold;}
    .userinfo-inner{padding-left:10px;color:#fff;cursor:pointer}
</style>