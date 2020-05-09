<template>
  <div style="display: inline-block">
    <el-dialog :visible.sync="dialog" :close-on-click-modal="false" :before-close="cancel" :title="title" append-to-body width="500px" @close="cancel">
        <el-form ref="form" :model="form" :rules="rules" size="small" label-width="88px">
            <el-form-item label="用户姓名" prop="username">
                <el-input v-model="form.username" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
            <el-form-item label="联系电话" prop="telphone">
                <el-input v-model="form.telphone" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
            <el-form-item label="工作单位" prop="company">
                <el-input v-model="form.company" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
            <el-form-item label="用户描述" prop="userdetail">
                <el-input v-model="form.userdetail" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button type="text" @click="cancel">取消</el-button>
            <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getUserInfo, addUserInfo } from '@/api/user/user'
import { isvalidPhone } from '@/utils/isvalid'
export default {

    mounted() {
        this.getUserInfomation()
    },
    data() {
        const validPhone=(rule, value,callback)=>{
            if (!value){
                callback(new Error('请输入电话号码'))
            }else  if (!isvalidPhone(value)){
                callback(new Error('请输入正确的11位手机号码'))
            }else {
                callback()
            }
        }
        return {
            loading: false,
            dialog: false, 
            title: '个人信息', 
            form: { username: '', telphone: '', company: '', userdetail: ''},
            rules: {
                telphone: [
                    { validator: validPhone, trigger: 'blur' } //这里需要用到全局变量
                ],
            }
        }
    },
    methods: {
        getUserInfomation() {
            var user = JSON.parse(sessionStorage.getItem("name"));
            getUserInfo(user).then(
                res=>{
                    let { code, data } = res
                    let { username, telphone, company, userdetail } = data
                    
                    this.form = { username: username, telphone: telphone, company: company, userdetail: userdetail}
                }
            )
        },
        
        cancel() {
            this.resetForm()
        },

        doSubmit() {
            addUserInfo(this.form).then(
                res => {
                    let {code,msg} = res
                    if(code == 200){
                        this.dialog = false
                        this.getUserInfomation()
                    }
                }
            )

        },

        resetForm() {
            this.dialog = false
            this.form = { username: '', telphone: '', company: '', userdetail: ''}
        }

    }

    
}
</script>
<style>

</style>
