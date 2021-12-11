<template>
  <div class="about">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">About us</h1>
        <h2 class="subtitle">Learn about us more</h2>
      </div>
    </div>
    <div class="section">
      <div class="container">
        This platform is a training one for your education, you can study not going out of home
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  mounted() {
    document.title = 'About | StudyNet'
  }
}
</script>