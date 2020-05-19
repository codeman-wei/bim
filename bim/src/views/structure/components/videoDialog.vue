<template>
  <el-dialog append-to-body :close-on-click-modal="false" :before-close="cancel" :visible.sync="dialog" width="50%" @close="cancel">
    <div class="video-div">
      <div style="display: flex;justify-content: space-around; padding: 20px">
        <el-button :disabled="pathValid('up')"  class="filter-item" size="mini" type="primary" icon="el-icon-caret-top" @click="getVideoPath('up')">前</el-button>
        <el-button :disabled="pathValid('bottom')"  class="filter-item" size="mini" type="primary" icon="el-icon-caret-bottom" @click="getVideoPath('bottom')">后</el-button>
        <el-button :disabled="pathValid('left')"  class="filter-item" size="mini" type="primary" icon="el-icon-caret-left" @click="getVideoPath('left')">左</el-button>
        <el-button :disabled="pathValid('right')"  class="filter-item" size="mini" type="primary" icon="el-icon-caret-right" @click="getVideoPath('right')">右</el-button>
      </div>
      <video
        :src="videoPath"
        controls="controls"
        style="width: 100%"
        align="center">
          您的浏览器不支持视频播放
      </video>
    </div>
    <span slot="footer" class="dialog-footer">
      <el-button style="margin-left: 10px;" size="small" type="primary" @click="toUpload">上传视频</el-button>
    </span>
    <uploadVideo ref="uploadVideo" :id="data.id" :belong="belong" />
  </el-dialog>
</template>
<script>
import uploadVideo from '@/views/structure/uploadVideo'
export default {
  props: {
    data: {
      type: Object,
      required: true
    },
    belong: {
      type: String,
      required: true
    }
  },
  components: {
    "uploadVideo": uploadVideo
  },
  data() {
    return {
      videoPath: '',
      dialog: false,
    };
  },
  methods: {
    getVideoPath(pos) {
      switch (pos) {
        case 'left': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.data.videoLeftUrl
          break;
        case 'up': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.data.videoUpUrl
          break;
        case 'right': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.data.videoRightUrl
          break;
        case 'bottom': this.videoPath = 'http://127.0.0.1:5000/static/video' + this.data.videoBottomUrl
          break;
      }
    },
    cancel() {
      this.videoPath = ''
      this.dialog = false
    },
    toUpload() {
      this.$refs.uploadVideo.dialog = true
    },
    pathValid(pos) {
      var path
      switch (pos) {
        case 'left': path = this.data.videoLeftUrl
          break;
        case 'up': path = this.data.videoUpUrl
          break;
        case 'right': path = this.data.videoRightUrl
          break;
        case 'bottom': path = this.data.videoBottomUrl
          break;
      }
      return path === null || path === ''
    }
  }
}
</script>
