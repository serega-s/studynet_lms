<template>
  <div class="create-course">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Create course</h1>
      </div>
    </div>
    <section class="section">
      <div class="columns is-centered">
        <div class="column is-8">
          <div class="mb-6 px-6 py-4 has-background-grey-lighter">
            <h2 class="subtitle">Meta information</h2>
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
          </div>
          <div class="mb-6 px-6 py-4 has-background-grey-lighter">
            <h2 class="subtitle">Lessons</h2>

            <button class="button is-primary" @click="addLesson">
              Add lesson
            </button>

            <div
              v-for="(lesson, index) in form.lessons"
              :key="index"
              class="mb-4"
            >
              <h3 class="subtitle is-size-6">Lesson</h3>

              <div class="field">
                <label for="title">Title</label>
                <input type="text" class="input" v-model="lesson.title" />
                <!-- :name="form.lessons[index][title]" -->
              </div>

              <div class="field">
                <label for="short_description">Short description</label>
                <textarea
                  type="text"
                  class="input"
                  v-model="lesson.short_description"
                />
                <!-- :name="form.lessons[index][short_description]" -->
              </div>

              <div class="field">
                <label for="long_description">Long description</label>
                <textarea
                  type="text"
                  class="textarea"
                  v-model="lesson.long_description"
                />
                <!-- :name="form.lessons[index][long_description]" -->
              </div>
            </div>

            <hr />
          </div>

          <div class="field buttons">
            <button class="button is-success m-1" @click="submitForm('draft')">
              Save as draft
            </button>
            <button class="button is-info m-1" @click="submitForm('in_review')">
              Submit for review
            </button>
          </div>
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
        status: "",
        lessons: [
          {
            title: "",
            short_description: "",
            long_description: "",
          },
        ],
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
    async submitForm(status) {
      this.$store.commit("setIsLoading", true)
      this.form.status = status
      try {
        const response = await CourseService.createCourse(this.form)
        console.log(response.data)
      } catch (e) {
        console.error(e.response)
      }
      this.$store.commit("setIsLoading", false)
    },

    addLesson() {
      this.form.lessons.push({
        title: "",
        short_description: "",
        long_description: "",
      })
    },
  },
}
</script>
