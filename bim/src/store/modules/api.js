// const baseUrl = process.env.VUE_APP_BASE_API
const baseUrl = 'http://127.0.0.1:5000/static'
const api = {
  state: {
    // 图片上传
    imagesUploadApi: baseUrl + '/api/pictures',
    // Sql 监控
    sqlApi: baseUrl + '/druid',
    // swagger
    swaggerApi: baseUrl + '/swagger-ui.html',
    // 文件上传
    fileUploadApi: baseUrl + '/api/localStorage',
    // baseUrl，
    baseApi: baseUrl,
    imageApi: baseUrl + '/image'
  }
}

export default api
