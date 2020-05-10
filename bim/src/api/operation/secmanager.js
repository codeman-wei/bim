import request from '@/utils/request'

export function getAll(param) {
    return request(
    {
      url: '/secmanager/',
      method:'get',
      params: param
    })
}

export function add(data) {
  return request(
    {
      url: '/secmanager/add',
      method:'post',
      data
    }
  )
}

export function edit(data) {
  return request(
    {
      url: '/secmanager/edit',
      method:'put',
      data
    }
  )
}

export function del(id) {
  return request(
    {
      url: '/secmanager/del/' + id,
      method: 'delete',
    }
  )
}
