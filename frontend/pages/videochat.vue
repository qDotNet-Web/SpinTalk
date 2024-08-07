<template>
    <div class="main-app">
        <Card style="width: 100%" class="mt-2 mb-2">
            <template #content>
                <div class="iconBox mb-3 flex-row justify-start" style="display: inline-flex;">
                    <i class="pi pi-video text-5xl is-size-50 is-primary-color"></i>
                    <h3 style="margin: 0">Video</h3>
                </div>
                <div class="videosContainer mb-1">
                    <div class="video-player" id="video-other">
                        <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9a494b12-0ae6-4522-99c0-b4b7f08d9047/d9r0qpv-0badc01c-1db9-4146-9361-e869b3931d43.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzlhNDk0YjEyLTBhZTYtNDUyMi05OWMwLWI0YjdmMDhkOTA0N1wvZDlyMHFwdi0wYmFkYzAxYy0xZGI5LTQxNDYtOTM2MS1lODY5YjM5MzFkNDMuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.gQqGDe7alC-Lo27L2vjTmrRBpk4MyAiKSu4Ykpa896c" alt="">
                        <div class="speed-dial"><speedDialVideo></speedDialVideo></div> 
                    </div>
                    <div class="video-player" id="video-self">
                        <video ref="video" class="video-self"/>
                    </div>
                </div>
                <div class="flex-row flex-center gap-1 mb-3">
                    <Button label="Next" icon="pi pi-arrow-up-right" outlined />
                    <Button label="Random" severity="warning" icon="pi pi-refresh" outlined />
                    <Button label="Filter" icon="pi pi-star" severity="help" outlined />
                </div>
            </template>
        </Card>

        <textChat></textChat>

    </div>
</template>

<script>
export default {
    middleware: 'auth',
    data() {
        return {
            mediaStream: ref(null),
            imageData: {
                image: '',
                image_orientation: 0,
            },
        }
    },
    async beforeRouteLeave(to, from, next) {
        this.stopVideos();
        next();
        
    },
    mounted() {
            navigator.mediaDevices.getUserMedia({video: true})
            .then(mediaStream => {
                    this.mediaStream = mediaStream                   
                    this.$refs.video.srcObject = mediaStream;
                    this.$refs.video.play()
            })
        
            
    },
    methods: {
        takePicture() {
            const canvas = document.createElement('canvas');
            canvas.width = this.$refs.video.videoWidth;
            canvas.height = this.$refs.video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(this.$refs.video, 0, 0, canvas.width, canvas.height);
            this.imageData.image = canvas.toDataURL('image/png');
            this.imageData.image_orientation = 0;
        },
        stopVideos() {
            this.mediaStream.getTracks().forEach(track => track.stop());
        }
    }
}
</script>