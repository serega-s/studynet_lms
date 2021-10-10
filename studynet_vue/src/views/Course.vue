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
                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
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

                  <hr />

                  <article
                    class="media"
                    v-for="comment in comments"
                    :key="comment.id"
                  >
                    <div class="media-content">
                      <div class="content">
                        <!-- <p> -->
                        <strong>{{ comment.name }}</strong> ||
                        {{ comment.created_at }}
                        <br />
                        <blockquote>{{ comment.content }}</blockquote>
                        <!-- </p> -->
                      </div>
                    </div>
                  </article>

                  <form @submit.prevent="submitComment">
                    <div class="field">
                      <label for="name">Name</label>
                      <div class="control">
                        <input
                          type="text"
                          class="input"
                          placeholder="Name"
                          v-model="comment.name"
                        />
                      </div>
                    </div>
                    <div class="field">
                      <label for="content">Content</label>
                      <div class="control">
                        <input
                          type="text"
                          class="input"
                          placeholder="Content"
                          v-model="comment.content"
                        />
                      </div>
                    </div>
                    <div class="field">
                      <div class="control">
                        <button class="button is-link">Submit</button>
                      </div>
                    </div>
                  </form>
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
      comments: [],
      comment: {
        name: "",
        content: "",
      },
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
  methods: {
    submitComment() {
      const data = {
        name: this.comment.name,
        content: this.comment.content,
      }

      axios
        .post(
          `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/`,
          data
        )
        .then((response) => {
          this.comment.name = ""
          this.comment.content = ""
          this.comments = []
          this.getComments()
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson
      this.getComments()
    },
    getComments() {
      axios
        .get(
          `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/get-comments/`
        )
        .then((response) => {
          this.comments = response.data
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
  },
}
</script>
