<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">My Account</h1>
      </div>
    </div>

    <section class="section">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="subtitle is-size-3">Your active courses</h2>
        </div>
        <div v-for="course in courses" :key="course.id" class="column is-4">
          <CourseItem :course="course"/>
        </div>
      </div>
      <button class="button is-warning is-outline" @click="logout()">
        Log out
      </button>
    </section>
  </div>
</template>

<script>
import ActivityService from "../../services/activity.service"
import CourseItem from "@/components/CourseItem"

export default {
  name: "MyAccount",
  components: {CourseItem},
  data() {
    return {
      courses: []
    }
  },
  mounted() {
    document.title = "My Account | StudyNet"

    this.getActiveCourses()
  },
  methods: {
    logout() {
      this.$store.commit("setIsLoading", true)
      this.$store.dispatch("logout").then(
          () => {
            this.$router.push({name: "LogIn"})
          },
          (error) => {
            console.log(error.response)
          }
      )
      this.$store.commit("setIsLoading", false)
    },
    async getActiveCourses() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await ActivityService.getActiveCourses()
        this.courses = response.data
      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    }
  },
}
</script>

<style></style>
