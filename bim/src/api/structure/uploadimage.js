import request from '@/utils/request'


export function upload(data, config) {
    console.log(data)
    return request({
      url: 'upload/img',
      method: 'post',
      data,
      config
    })
  }