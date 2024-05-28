<template>
    <div class="iconBox mb-3" style="display: inline-flex;">
        <i class="pi pi-video text-5xl is-size-100 is-primary-color"></i>
    </div>
    <div class="flex-row mb-3">
        <div id="el" class="video-box">
            <video v-if="!imageData.image" ref="video" class="video-chatBox" />
            <speedDialVideo></speedDialVideo>
        </div>
        <div class="video-box">
            <div class="iconBox" style="display: inline-flex; padding-top: 7rem;">
                <i class="pi pi-video text-5xl is-size-100"></i>
            </div>
        </div>
    </div>
    <div class="flex-row flex-start gap-1 mb-3">
        <Button label="Next" icon="pi pi-arrow-up-right" outlined />
        <Button label="Random" severity="warning" icon="pi pi-refresh" outlined />
        <Button label="Filter" icon="pi pi-star" severity="help" outlined />
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