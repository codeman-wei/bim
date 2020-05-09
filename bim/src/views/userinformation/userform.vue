<template>
    <el-dialog :visible.sync="dialog" 
        :close-on-click-modal="false" 
        :before-close="cancel"
        :title="isAdd ? '新增用户信息' : '编辑用户信息'" 
        append-to-body 
        width="500px" 
        @close="cancel">
        <el-form ref="form" :model="form" :rules="rules" size="small" label-width="88px">
            <el-form-item label="用户名称" prop="userName">
                <el-input v-model="form.userName" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
            <el-form-item label="密码" prop="userPassword">
                <el-input v-model="form.userPassword" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>                        
            <el-form-item label="用户描述" prop="userDetail">
                <el-input v-model="form.userDetail" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button type="text" @click="cancel">取消</el-button>
            <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
        </div>
    </el-dialog>
</template>
<script>
import { addUser,showAllUser } from '@/api/user/user'
export default {
    props: {
      isAdd: {
        type: Boolean,
        required: true
      }
    },
    data() {
        return {
            loading: false,
            dialog: false,
            rules: {
                userName: [
                    { required: true, message: '请输入用户名称', trigger: 'blur' },
                    { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
                ],
                userPassword: [
                    { required: true, message: '请输入用户密码', trigger: 'blur' },
                    { min: 6, message: '长度不小于6个字符', trigger: 'blur' }
                ],
            },
            form: {
                id: '',
                userName: '',
                userPassword: '',
                userDetail: ''
            },
        }
    },
    methods: {
        cancel() {
            this.resetForm("form")
            this.dialog = false
        },
        doSubmit() {
            this.$refs['form'].validate((valid) => {
                if (valid) {
                    this.loading = true
                    if (this.isAdd) {
                        this.doAdd()
                    } 
                    else {
                        this.doEdit()
                    }
                } else {
                    return false
                }
            })
        },
        doAdd() {
            addUser(this.form).then(res => {
                this.dialog = false
                this.resetForm('form')
                this.$notify({
                    title: '添加成功',
                    type: 'success',
                    duration: 2500
                })
                this.loading = false
                this.$parent.initData()
            }).catch(err => {
                this.loading = false
            })
        },
        
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
        
    }
}
</script>