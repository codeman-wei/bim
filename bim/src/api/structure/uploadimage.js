import request from '@/utils/request'


export function upload(data, config) {
  console.log(data)
  return request({
    url: 'upload/uploadImg',
    method: 'post',
    data,
    config
  })
}

export function edit(data, config) {
  console.log(data)
  return request({
    url: 'upload/editImg',
    method: 'put',
    data,
    config
  })
}