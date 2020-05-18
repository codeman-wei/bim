import request from '@/utils/request'


export function upload(data, config) {
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

export function uploadFiles(data) {
  return request({
    url: 'upload/file',
    method: 'post',
    data
  })
}

export function uploadVideo(data) {
  return request({
    url: 'upload/video',
    method: 'post',
    data
  })
}