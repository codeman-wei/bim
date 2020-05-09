<template>
    <div class="login">
        <div class = "header">
            <div class="title">
                <h1>平潭海峡公铁两用大桥附属设施运维管控系统</h1>
                <h4>Operation and maintenance system for auxiliary facilities of Pingtan Cross-Strait Highway-Railway Bridge</h4>
            </div>
        </div>
        <div class="main">
            <el-row >
                <el-col :offset="15">
                    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-position="left" label-width="0px" class="login-form">
                        <h3 class="loginTab">用户登录
                        </h3>
                        <el-form-item prop="username">
                            <el-input v-model="loginForm.username" type="text" auto-complete="off" placeholder="账号" prefix-icon="el-icon-user">
                            </el-input>
                        </el-form-item>
                        <el-form-item prop="password">
                            <el-input v-model="loginForm.password" type="password" auto-complete="off" placeholder="密码" prefix-icon="el-icon-lock" @keyup.enter.native="handleLogin">
                            </el-input>
                        </el-form-item>

                        <el-form-item style="width:100%;">
                            <el-button :loading="loading" size="medium" type="primary" style="width:100%;" @click.native.prevent="handleLogin">
                            <span v-if="!loading">登 录</span>
                            <span v-else>登 录 中...</span>
                            </el-button>
                        </el-form-item>
                    </el-form>

                </el-col>
            </el-row>
        </div>
        <div class="footer">
        </div>
    </div>
</template>
<script>
import { login } from '@/api/login'
export default {
    data() {
        return {
            loginForm: {
                username: '',
                password: '',
            },
            loading: false,
            loginRules: {
                username: [{ required: true, trigger: 'blur', message: '用户名不能为空' }],
                password: [{ required: true, trigger: 'blur', message: '密码不能为空' }],
            },
            redirect: undefined
        }
    },
    watch: {
        $route: {
            handler: function(route) {
                this.redirect = route.query && route.query.redirect
            },
            immediate: true
        }
    },
    mounted() {
		var token = sessionStorage.getItem('token');
		if (token) {
            sessionStorage.setItem('token', token);
            this.$router.push({ path: '/home' });
        }
    },
    methods: {
        handleLogin() {
            this.$refs.loginForm.validate(valid => {
                const user = {
                    username: this.loginForm.username,
                    password: this.loginForm.password,
                }
                if(valid) {
                    this.loading = true
                    this.$store.dispatch('Login', user).then(()=>{
                        this.loading = false
                        this.$router.push({ path: this.redirect || '/home' }) // 登录成功之后重定向到首页
                    })
                    .catch(() => {
                        this.loading = false
                        this.getCode()
                     })
                }
                else {
                    console.log('error submit!!') // 登录失败提示错误
                    return false
                }
            })
        }
    }
}
</script>
<style>

    .login {
        position: fixed;
        height: 100%;
        width: 100%;
        background-image: url(../assets/login.jpg);
        background-size: cover;
    }
    .header {
        margin-bottom: 60px;
    }
    /* .header, .footer {
        width: 100%;
        height: 25%;
    } */
    /* .main {
        width: 100%;
        height: 40%;
    } */

    .title {
        padding: 25px 0 0 20px;
        color: white;
        font-size: 20px;
    }

    .login-form {
        border-radius: 6px;
        background: white;
        width: 280px;
        padding: 25px 25px 5px 25px;
    }

    .loginTab {
        margin: 0 auto 25px auto;
        text-align: center;
        color: #707070;
    }

    .login-form .el-input {
        height: 38px;
    }
    .login-form .el-input input {
        height: 38px;
    }
    .login-form .input-icon{
        height: 39px;width: 14px;margin-left: 2px;
    }

</style>