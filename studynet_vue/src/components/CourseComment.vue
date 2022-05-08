<template>
  <article
      class="media box"
  >
    <div class="media-content">
      <div class="content">
        <strong>{{ comment.name }}</strong> ||
        {{ comment.created_at }}
        <br/>
        <blockquote>{{ comment.content }}</blockquote>
      </div>
    </div>
  </article>
</template>

<script>
export default {
  name: "CourseComment",
  props: ["comment"]
}
</script>

<style scoped>

</style>