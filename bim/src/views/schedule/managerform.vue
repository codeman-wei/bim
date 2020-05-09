<template>
    <el-dialog :visible.sync="dialog" 
            :close-on-click-modal="false" 
            :before-close="cancel" 
            :title="isAdd? '新增项目':'编辑项目'" 
            append-to-body 
            width="500px"  
            @close="cancel">
        <!-- <el-form ref="form" :model="form" :rules="rules" size="small" label-width="88px">
            <el-form-item label="施工流程" prop="userName">
                <el-input v-model="form.userName" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
            <el-form-item label="活动时间">
                <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
                </el-col>
                <el-col class="line" :span="2">-</el-col>
                <el-col :span="11">
                <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
                </el-col>
            </el-form-item>                   
            <el-form-item label="当前状态" prop="userDetail">
                <el-input v-model="form.userDetail" type="text" auto-complete="on" style="width: 370px;" />
            </el-form-item>
        </el-form> -->
        <div slot="footer" class="dialog-footer">
            <el-button type="text" @click="cancel">取消</el-button>
            <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
        </div>
    </el-dialog>

</template>
<script>
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
            dialog: false
        }
    },
    methods: {
        cancel() {
            this.dialog = false
        },
        doSubmit() {},
    }
}
</script>
<style>

</style>