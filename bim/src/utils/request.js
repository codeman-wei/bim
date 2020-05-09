import axios from 'axios'
import { Notification, MessageBox } from 'element-ui'
import store from '../store'
import router from '@/router/index'
// 创建axios实例
const service = axios.create({
    baseURL: 'http://127.0.0.1:5000/', // api 的 base_url
    timeout: 1200000 // 请求超时时间
  })


// 添加请求拦截器
service.interceptors.request.use(
    // 在发送请求之前做些什么
    config => {
        var token = sessionStorage.getItem('token');
        if (token) {  // 判断是否存在token，如果存在的话，则每个http header都加上token
            token = sessionStorage.getItem('token')+':';
            config.headers.Authorization = `Basic ${new Buffer(token).toString('base64')}`;
        }
        config.headers['Content-Type'] = 'application/json'
        return config
    },
    // 对请求错误做些什么
    error => {
        console.log(error)
        Promise.reject(error);
    }
)

// 添加响应拦截器
service.interceptors.response.use(
    // 对响应数据做点什么
    response => {
        const code = response.status
        if (code < 200 || code > 300) {
          Notification.error({
            title: response.message
          })
          return Promise.reject('error')
        } else {
          return response.data
        }
    },
    // 对响应错误做点什么
    error => {
        let code = 0
        try {
            code = error.response.status
        } catch (e) {
            if (error.toString().indexOf('Error: timeout') !== -1) {
              Notification.error({
                title: '网络请求超时',
                duration: 5000
              })
              return Promise.reject(error)
            }
        }
        if (code) {
            if (code === 401) {
                MessageBox.confirm(
                    '登录状态已过期，您可以继续留在该页面，或者重新登录',
                    '系统提示',
                    {
                    confirmButtonText: '重新登录',
                    cancelButtonText: '取消',
                    type: 'warning'
                    }
                ).then(() => {
                    store.dispatch('LogOut').then(() => {
                        router.push({ path: '/' })
                        location.reload() // 为了重新实例化vue-router对象 避免bug
                    })
                })
            } 
            else if (code === 403) {
                router.push({ path: '/401' })
            } 
            else {
                const errorMsg = error.response.data.message
                if (errorMsg !== undefined) {
                    Notification.error({
                    title: errorMsg,
                    duration: 5000
                    })
                }
            }
        } 
        else 
        {
            Notification.error({
              title: '接口请求失败',
              duration: 5000
            })
        }
        return Promise.reject(error)
    }
)


//     function (response) {
//     // 对响应数据做点什么
//     return response;
// }, function (error) {
//     // 对响应错误做点什么
//     return Promise.reject(error);
// });

// 最后暴露实例
export default service