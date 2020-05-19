import request from '@/utils/request'


export function showAllProject(params){
    return request({
      url:'/project/',
      method:'get',
      params
    })
}

export function addProject(data, config){
  return request({
    url:'/project/addProject',
    method: 'post',
    data,
    config
  })
}

export function editProject(data, config){
  return request({
    url:'/project/editProject',
    method: 'put',
    data,
    config
  })
}