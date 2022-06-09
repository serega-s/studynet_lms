<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">
          {{ created_by.first_name }} {{ created_by.first_name }}
        </h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4" v-for="course in courses" :key="course.id">
            <CourseItem :course="course" />
          </div>

          <div class="column is-12">
            <nav class="pagination">
              <a class="pagination-previous">Previous</a>
              <a class="pagination-next">Next</a>
            </nav>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import CourseItem from "../components/CourseItem.vue"
import CourseService from "../services/course.service"
export default {
  components: { CourseItem },
  name: "Courses",
  data() {
    return {
      courses: [],
      created_by: {
        first_name: "",
        last_name: "",
      },
    }
  },
  mounted() {
    this.getCategories()
    this.getCourses()
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
    async getCourses() {
      this.$store.commit("setIsLoading", true)

      try {
        const response = await CourseService.getCourses(
          `courses/get-author-courses/${this.$route.params.id}`
        )
        this.courses = response.data.courses
        this.created_by = response.data.created_by
      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
