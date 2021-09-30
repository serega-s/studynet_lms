<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course.title }}</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h2>Table of content</h2>

            <ul>
              <li v-for="lesson in lessons" :key="lesson.id">
                <a @click="activeLesson = lesson">{{ lesson.title }}</a>
              </li>
            </ul>
          </div>

          <div class="column is-10">
            <!-- <h2>Cours</h2> -->

            <p>
              <template v-if="$store.state.user.isAuthenticated">
                <template v-if="activeLesson">
                  <h2>{{ activeLesson.title }}</h2>
                  {{ activeLesson.long_description }}
                </template>
                <template v-else>
                  {{ course.long_description }}
                </template>
              </template>
              <template v-else>
                <h2>Restricted access</h2>

                <p>You need to have an account to continue!</p>
              </template>
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "Course",
  data() {
    return {
      course: {},
      lessons: {},
      activeLesson: null,
    }
  },
  mounted() {
    const slug = this.$route.params.slug
    axios
      .get(`/api/v1/courses/${slug}/`)
      .then((response) => {
        this.course = response.data.course
        this.lessons = response.data.lessons
      })
      .catch((error) => {
        console.log(error.response)
      })
  },
}
</script>
