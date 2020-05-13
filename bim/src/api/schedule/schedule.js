import request from '@/utils/request'


export function showAllProject(params){
    return request({
      url:'/project/',
      method:'get',
      params
    })
}