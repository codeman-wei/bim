import request from '@/utils/request'

export function getProjectInfo(params){
  return request({
    url:'/employee/projectInfo',
    method:'get',
    params
  })
}

export function getEmpInfoByPID(params){
  return request({
      url:'/employee/empInfoBypid',
      method:'get',
      params
    })
}

export function addEmpInfo(params){
  return request({
      url:'/employee/addempinfo',
      method: 'POST',
      data:params
  })
}

export function editEmpInfo(params){
  return request({
      url: '/employee/editempinfo',
      method: 'PUT',
      data: params
  })
}

export function deleteEmpInfo(id){
  return request({
      url: '/employee/deleteempinfo/'+ id,
      method: 'delete',
  })
}

export function deleteBatchEmpInfo(param) {
  return request(
    {
      url: '/employee/deletebatchempinfo',
      method: 'post',
      data: param
    }
  )
}