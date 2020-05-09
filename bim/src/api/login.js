import request from '@/utils/request'

export function login(username, password) {
    return request({
      url: '/login',
      method: 'post',
      auth: {
          username,
          password
      }
    })
}