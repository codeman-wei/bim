import request from '@/utils/request'

export function getTree(param) {
    return request(
    {
      url: '/structure/tree',
      method:'get',
      params: param
    })
}