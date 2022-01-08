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
            <p>
              <template v-if="$store.state.user.isAuthenticated">
                <template v-if="activeLesson">
                  <h2>{{ activeLesson.title }}</h2>
                  {{ activeLesson.long_description }}

                  <hr />

                  <template v-if="activeLesson.lesson_type === 'quiz'">
                    <h3>{{ quiz.question }}</h3>

                    <div class="control">
                      <div class="radio">
                        <input
                          type="radio"
                          :value="quiz.op1"
                          v-model="selectedAnswer"
                        />
                        {{ quiz.op1 }}
                      </div>
                    </div>
                    <div class="control">
                      <div class="radio">
                        <input
                          type="radio"
                          :value="quiz.op2"
                          v-model="selectedAnswer"
                        />
                        {{ quiz.op2 }}
                      </div>
                    </div>
                    <div class="control">
                      <div class="radio">
                        <input
                          type="radio"
                          :value="quiz.op3"
                          v-model="selectedAnswer"
                        />
                        {{ quiz.op3 }}
                      </div>
                    </div>
                    <div class="control mt-4">
                      <button class="button is-info" @click="submitQuiz">
                        Submit
                      </button>
                    </div>
                    <template v-if="quizResult == correctAnswer">
                      <div class="notification is-success mt-4">
                        Correct :-D
                      </div>
                    </template>
                    <template v-else-if="quizResult == incorrectAnswer">
                      <div class="notification is-danger mt-4">
                        Wrong... Please try again!
                      </div>
                    </template>
                  </template>

                  <template v-if="activeLesson.lesson_type === 'article'">
                    <article
                      class="media box"
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

                      <div
                        class="notification is-danger"
                        v-for="error in errors"
                        :key="error"
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
import CourseService from '../services/course.service'
export default {
  name: "Course",
  data() {
    return {
      course: {},
      lessons: {},
      quiz: {},
      selectedAnswer: "",
      quizResult: null,
      activeLesson: null,
      correctAnswer: "Correct",
      incorrectAnswer: "Incorrect",
      errors: [],
      comments: [],
      comment: {
        name: "",
        content: "",
      },
    }
  },
  async mounted() {
    const slug = this.$route.params.slug

    await CourseService.getCoursesLessonsData(slug).then((response) => {
      this.course = response.data.course
      this.lessons = response.data.lessons
      
    })
    document.title = this.course.title
      ? this.course.title
      : "Restricted Access" + " | StudyNet"
  },
  methods: {
    submitComment() {
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
        CourseService.submitComment(this.course.slug, this.activeLesson.slug, data)
          .then((response) => {
            this.comment.name = ""
            this.comment.content = ""

            this.comments.push(response.data)
          })
          .catch((error) => {
            console.log(error.response)
          })
      }
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson
      if (lesson.lesson_type === "quiz") {
        this.getQuiz()
      } else {
        this.getComments()
      }
    },
    getQuiz() {
      CourseService.getQuiz(this.course.slug, this.activeLesson.slug)
        .then((response) => {
          this.quiz = response.data
        })
    },
    getComments() {
      CourseService.getComents(this.course.slug, this.activeLesson.slug)
        .then((response) => {
          this.comments = response.data
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
    submitQuiz() {
      this.quizResult = null

      if (this.selectedAnswer) {
        if (this.selectedAnswer === this.quiz.answer) {
          this.quizResult = this.correctAnswer
        } else {
          this.quizResult = this.incorrectAnswer
        }
      } else {
        alert("Select answer first please")
      }
    },
  },
}
</script>
