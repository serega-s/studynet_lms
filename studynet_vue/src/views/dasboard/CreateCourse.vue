<template>
  <div class="create-course">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Create course</h1>
      </div>
    </div>
    <section class="section">
      <div class="columns is-centered">
        <div class="column is-6">
          <form @submit.prevent="submitForm">
            <div class="field">
              <label for="title">Title</label>
              <input type="text" class="input" v-model="form.title" />
            </div>
            <div class="field">
              <label for="description">Short Description</label>
              <textarea
                v-model="form.short_description"
                class="textarea"
              ></textarea>
            </div>
            <div class="field">
              <label for="description">Long Description</label>
              <textarea
                v-model="form.long_description"
                class="textarea"
              ></textarea>
            </div>
            <div class="field">
              <div class="select is-multiple">
                <select multiple size="10" v-model="form.categories">
                  <option
                    v-for="category of categories"
                    :value="category.id"
                    :key="category.id"
                    >{{ category.title }}</option
                  >
                </select>
              </div>
            </div>
            <div class="field">
              <button class="button is-success">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios"
import CourseService from "../../services/course.service"
export default {
  data() {
    return {
      form: {
        title: "",
        short_description: "",
        long_description: "",
        categories: [],
      },

      categories: [],
    }
  },
  mounted() {
    this.getCategories()
  },
  methods: {
    async getCategories() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await CourseService.getCategories()
        this.categories = response.data
      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await CourseService.createCourse(this.form)
        console.log(response.data)
      } catch (e) {
        console.error(e.response)
      }
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
