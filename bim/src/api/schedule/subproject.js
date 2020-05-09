import request from '@/utils/request'


export function getSubprojectById(id){
    return request({
      url: '/project/subproject',
      method:'get',
      params:{
          id
      }
    })
}