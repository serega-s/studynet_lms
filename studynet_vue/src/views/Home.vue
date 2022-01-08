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

              <h2 class="is-size-2 mt-4 mb-4">Study at your own place</h2>

              <p>This is just some random placeholder</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="far fa-comments"></i
              ></span>

              <h2 class="is-size-2 mt-4 mb-4">Study with others</h2>

              <p>This is just some random placeholder</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="fas fa-home"></i
              ></span>

              <h2 class="is-size-2 mt-4 mb-4">Study from your home</h2>

              <p>This is just some random placeholder</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <router-link to="/sign-up" class="button is-info is-size-3 mt-6 mb-6"
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
import CourseService from '../services/course.service'

export default {
  components: { CourseItem },
  name: "Home",
  data() {
    return {
      courses: [],
    }
  },
  mounted() {
    document.title = 'Welcome | StudyNet'
    CourseService.getFrontpageCourses()
      .then((response) => {
        this.courses = response.data
      })
      .catch((error) => {
        console.log(error.response)
      })
  },
}
</script>
