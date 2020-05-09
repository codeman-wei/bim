import request from '@/utils/request'

export function addUser(param) {
    return request({
      url: '/user/addUser',
      method: 'post',
      data: param
    })
}

export function showAllUser(param){
  return request({
    url:'/user/',
    method:'get',
    params:param
  })
}

export function getUserInfo(loginname){
  return request({
    url:'/user/getUserInfo/' + loginname,
    method:'get',
  })
}

export function addUserInfo(param){
  return request({
    url:'/user/addUserInfo',
    method:'put',
    data: param
  })
}

export function editPassword(param){
  return request({
    url:'/user/editPassword',
    method:'put',
    data: param
  })
}

export function ResetPassword(id) {
  return request({
    url:'/user/resetPassword',
    method: 'put',
    data: { id }
  })
}

export function DeleteUser(id) {
  return request(
    {
      url: '/user/deleteUser/' + id,
      method: 'delete',
    }
  )
}

export function batchResetPassword(param) {
  return request(
    {
      url: '/user/batchresetPassword',
      method: 'post',
      data: param,
    }
  )
}


export function deleteBatchUser(param) {
  return request(
    {
      url: '/user/deleteBatchuser',
      method: 'post',
      data: param,
    }
  )
}

























