import request from '@/utils/request'

export function getlogs(params) {
    return request(
    {
      url: '/upload/updatelist',
      method:'get',
      params
    })
}