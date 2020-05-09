import request from '@/utils/request'


export function showAllProject(){
    return request({
      url:'/project/',
      method:'get',
    })
}