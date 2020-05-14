import request from '@/utils/request'

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

export function delAll(data) {
  return request(
    {
      url: '/secmanager/delAll',
      method: 'delete',
      data
    }
  )
}

export default { add, edit, del, delAll }

export function loadTree() {
  return request(
    {
      url: '/secmanager/test2',
      method: 'get',

    }
  )
}
