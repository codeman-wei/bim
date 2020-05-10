import request from '@/utils/request'

export function getParticipantsInfo(params){
    return request({
      url:'/project/participantsinfo',
      method:'get',
      params
    })
}

export function getParticipantsInfoByPID(params){
    return request({
        url:'/project/participantsinfobypid',
        method:'get',
        params
      })
}

export function addParticipantsinfo(params){
    return request({
        url:'/project/addparticipantsinfo',
        method: 'POST',
        data:params
    })
}

export function editParticipantsinfo(params){
    return request({
        url: '/project/editparticipantsinfo',
        method: 'PUT',
        data: params
    })
}

export function deleteParticipantsinfo(id){
    return request({
        url: '/project/deleteparticipantsinfo/'+ id,
        method: 'delete',
    })
}

export function deleteBatchParticipantsinfo(param) {
    return request(
      {
        url: '/project/deletebatchparticipantsinfo',
        method: 'post',
        data: param
      }
    )
  }