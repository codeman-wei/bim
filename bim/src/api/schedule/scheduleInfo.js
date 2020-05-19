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
export function del(id) {
  return request({
    url: '/project/delsubproject/' +  id,
    method: 'DELETE'
  })
}

export function batchdel(data) {
  return request({
    url: '/project/delbatchproject',
    method: 'post',
    data
  })
}
