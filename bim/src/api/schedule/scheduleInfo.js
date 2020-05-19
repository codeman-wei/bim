import request from '@/utils/request'

export function getProjectScheduleInfo(params){
    return request({
      url:'/project/getProjectScheduleInfo',
      method:'get',
      params
    })
}


export function getsubProjectById(params){
  return request({
    url: '/project/subproject',
    method:'get',
    params
  })
}

export function addsubProject(params){
  return request({
      url:'/project/addsubproject',
      method: 'POST',
      data:params
  })
}

export function editsubProject(params){
  return request({
    url:'/project/editsubproject',
    method: 'put',
    data:params
})
}