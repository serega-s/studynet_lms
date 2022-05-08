<template>
  <div class="video-container">
    <iframe
        :src="'https://www.youtube.com/embed/' + youtube_id"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture;"
        allowfullscreen
        height="400"
        width="100%">

    </iframe>
  </div>
</template>

<script>
export default {
  props: ["youtube_id"]
}
</script>

<style scoped>

</style>