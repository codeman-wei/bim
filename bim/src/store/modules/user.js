import { login } from '@/api/login'


const user = {
    state: {

    },
    mutations: {
        SET_TOKEN: (state, token) => {
            state.token = token
        },
    },
    actions: {
        // 登录
        Login({ commit }, userInfo) {
            const username = userInfo.username
            const password = userInfo.password
            return new Promise((resolve, reject) => {
                login(username, password).then(res => {
                  
                //   setToken(res.token, rememberMe)
                  commit('SET_TOKEN', res.token)
                  sessionStorage.setItem('token', JSON.stringify(res.token));
                  sessionStorage.setItem('name', JSON.stringify(res.name));
                //   setUserInfo(res.user, commit)
                //   // 第一次加载菜单时用到， 具体见 src 目录下的 permission.js
                //   commit('SET_LOAD_MENUS', true)
                  resolve()
                }).catch(error => {
                  reject(error)
                })
              })
        },

        // 登出
        LogOut({ commit }) {
            return new Promise((resolve, reject) => {
            commit('SET_TOKEN', '')
            //removeToken()
            resolve()
            })
        },

    }

}

export default user