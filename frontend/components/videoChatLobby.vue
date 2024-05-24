<template>
    <div class="iconBox" style="display: inline-flex;">
        <i class="pi pi-video text-5xl is-size-100 is-primary-color"></i>
    </div>
    <h1>Random Video-Chat</h1>
    <div class="flex-row mb-3">
        <div id="el" class="video-box">
  
            <video v-if="!imageData.image" ref="video" />
        </div>
        <div class="video-box">
            <div class="iconBox" style="display: inline-flex; padding-top: 7rem;">
                <i class="pi pi-video text-5xl is-size-100"></i>
            </div>
        </div>
    </div>
    <div class="flex-row">
    </div>
</template>
<script>
export default {
    data() {
        return {
            mediaStream: null,
            imageData: {
                image: '',
                image_orientation: 0,
            },
        }
    },
    mounted() {
                navigator.mediaDevices.getUserMedia({video: true})
            .then(mediaStream => {
                    this.$refs.video.srcObject = mediaStream;
                    this.$refs.video.play()
                    this.mediaStream = mediaStream                   
            }) 
    },
}
</script>