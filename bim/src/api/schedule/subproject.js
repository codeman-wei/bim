import request from '@/utils/request'


export function getSubprojectById(id){
    return request({
      url: '/project/subproject',
      method:'get',
      params:{
          id
      }
    })
}



export function getProjectList(id){
  return request({
    url: '/project/list',
    method:'get'
  })
}