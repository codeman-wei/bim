import request from '@/utils/request'

export function getAllEmp(param) {
    return request(
    {
      url: '/employee/',
      method:'get',
      params: param
    })
}
export function addEmp(param) {
  return request(
    {
      url: '/employee/addEmp',
      method:'post',
      data: param
    }
  )
}

export function deleteEmp(id) {
  return request(
    {
      url: '/employee/deleteEmp/' + id,
      method: 'delete',
    }
  )
}

export function editEmp(param) {
  return request(
    {
      url: '/employee/editEmp',
      method: 'put',
      data: param
    }
  )
}

export function deleteBatchEmp(param) {
  return request(
    {
      url: '/employee/deleteBatchEmp',
      method: 'post',
      data: param
    }
  )
}