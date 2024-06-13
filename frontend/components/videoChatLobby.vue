<template>
    <div class="iconBox mb-3 flex-row justify-start" style="display: inline-flex;">
        <i class="pi pi-video text-5xl is-size-50 is-primary-color"></i>
        <h3 style="margin: 0">Video</h3>
    </div>
    <div class="flex-row mb-3">
        <div id="el" class="video-box">
            <video v-if="!imageData.image" ref="video" class="video-chatBox" />
            <speedDialVideo></speedDialVideo>
        </div>
        <div id="el" class="video-box">
            <video v-if="!imageData2.image" ref="video2" class="video-chatBox" />
            <speedDialVideo></speedDialVideo>
        </div>
    </div>
    <div class="flex-row flex-center gap-1 mb-3">
        <Button label="Next" icon="pi pi-arrow-up-right" outlined style="font-size: 1.3rem;" />
        <Button label="Random" severity="warning" icon="pi pi-refresh" outlined style="font-size: 1.3rem;" />
        <Button label="Filter" icon="pi pi-star" severity="help" outlined style="font-size: 1.3rem;" />
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
            mediaStream2: null,
            imageData2: {
                image: '',
                image_orientation: 0,
            },
        }
    },
    mounted() {
                navigator.mediaDevices.getUserMedia({video: true})
            .then(mediaStream => {
                    this.$refs.video.srcObject = mediaStream;
                    this.$refs.video.play();
                    this.mediaStream = mediaStream;               
            })
            navigator.mediaDevices.getUserMedia({video2: true})
            .then(mediaStream => {
                    this.$refs.video.srcObject = mediaStream2;
                    this.$refs.video.play();
                    this.mediaStream = mediaStream2;               
            }) 
    },
}
</script>