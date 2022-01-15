<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to StudyNet</h1>
        <h2 class="subtitle">An online place for learning what you want</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="far fa-clock"></i
              ></span>

              <h2 class="is-size-2 mt-4 mb-4">Study at your convenience</h2>

              <p>You can study at convenient time for you</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="far fa-comments"></i
              ></span>

              <h2 class="is-size-2 mt-4 mb-4">Study with others</h2>

              <p>Study with others and write the comments about courses</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="fas fa-home"></i
              ></span>

              <h2 class="is-size-2 mt-4 mb-4">Study from your home</h2>

              <p>You can get a additional education at home</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <router-link
              to="/sign-up"
              class="button is-info is-size-3 mt-6 mb-6"
              >Click to get started</router-link
            >
          </div>

          <hr />

          <div class="column is-3" v-for="course in courses" :key="course.id">
            <CourseItem :course="course" />
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
  name: "Home",
  data() {
    return {
      courses: [],
    }
  },
  mounted() {
    this.getFrontpageCourses()
    document.title = "Welcome | StudyNet"
  },
  methods: {
    async getFrontpageCourses() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await CourseService.getFrontpageCourses()
        this.courses = response.data
      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
