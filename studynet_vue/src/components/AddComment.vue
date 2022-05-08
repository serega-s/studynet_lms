<template>
  <form @submit.prevent="submitComment">
    <div class="field">
      <label for="name">Name</label>
      <div class="control">
        <input
            v-model="comment.name"
            class="input"
            placeholder="Name"
            type="text"
        />
      </div>
    </div>
    <div class="field">
      <label for="content">Content</label>
      <div class="control">
        <textarea v-model="comment.content" class="textarea" placeholder="Comment"></textarea>
      </div>
    </div>

    <div
        v-for="error in errors"
        :key="error"
        class="notification is-danger"
    >
      {{ error }}
    </div>

    <div class="field">
      <div class="control">
        <button class="button is-link">Submit</button>
      </div>
    </div>
  </form>
</template>

<script>
import CourseService from "@/services/course.service"

export default {
  name: "AddComment",
  props: ["course", "activeLesson"],
  data() {
    return {
      comment: {
        name: "",
        content: ""
      },
      errors: ""
    }
  },
  methods: {
    async submitComment() {
      this.$store.commit("setIsLoading", true)
      const data = {
        name: this.comment.name,
        content: this.comment.content,
      }

      this.errors = []

      if (!this.comment.name) {
        this.errors.push("The name must be filled out.")
      } else if (!this.comment.content) {
        this.errors.push("The content be filled out.")
      } else if (!this.errors.length) {
        try {
          const response = await CourseService.submitComment(
              this.$route.params.slug,
              this.activeLesson.slug,
              data
          )
          this.comment.name = ""
          this.comment.content = ""

          this.$emit("submitComment", response.data)
        } catch (e) {
          console.error(e)
        }
      }
      this.$store.commit("setIsLoading", false)
    },
  }
}
</script>

<style scoped>

</style>