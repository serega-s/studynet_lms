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
            <template v-if="$store.state.user.isAuthenticated">
              <div v-if="activeLesson">
                <h2>{{ activeLesson.title }}</h2>

                <span class="tag is-warning" v-if="activity.status === 'started'" @click="markAsDone">Started (mark as done)</span>
                <span class="tag is-success" v-else>Done</span>

                <hr>
                {{ activeLesson.long_description }}

                <hr/>

                <div v-if="activeLesson.lesson_type === 'quiz'">
                  <Quiz :quiz="quiz"/>
                </div>
                <div v-else-if="activeLesson.lesson_type === 'article'">
                  <CourseComment v-for="comment in comments" :key="comment.id" :comment="comment"/>

                  <AddComment :active-lesson="activeLesson" :course="course" @submitComment="submitComment"/>
                </div>
                <div v-else-if="activeLesson.lesson_type === 'video'">
                  <Video :youtube_id="activeLesson.youtube_id"/>
                </div>
                <div v-else>
                  {{ course.long_description }}
                </div>
              </div>
            </template>
            <template v-else>
              <h2>Restricted access</h2>

              <p>You need to have an account to continue!</p>
            </template>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import CourseService from "../services/course.service"
import ActivityService from "../services/activity.service"
import CourseComment from "@/components/CourseComment"
import AddComment from "@/components/AddComment"
import Quiz from "@/components/Quiz"
import Video from "@/components/Video"

export default {
  name: "Course",
  components: {Video, Quiz, AddComment, CourseComment},
  data() {
    return {
      course: {},
      lessons: {},
      quiz: {},
      activeLesson: null,
      errors: [],
      comments: [],
      activity: {}
    }
  },
  mounted() {
    this.getCoursesLessonsData()
  },
  methods: {
    async getCoursesLessonsData() {
      this.$store.commit("setIsLoading", true)
      const slug = this.$route.params.slug

      try {
        const response = await CourseService.getCoursesLessonsData(slug)
        this.course = response.data.course
        this.lessons = response.data.lessons

        document.title = this.course.title
            ? this.course.title
            : "Restricted Access" + " | StudyNet"

      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    },
    submitComment(comment) {
      this.comments.push(comment)
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson
      if (lesson.lesson_type === "quiz") {
        this.getQuiz()
      } else {
        this.getComments()
      }

      this.trackStarted()
    },
    async trackStarted() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await ActivityService.trackStarted(this.$route.params.slug, this.activeLesson.slug)
        this.activity = response.data
      } catch (e) {
        console.log(e)
      }
      this.$store.commit("setIsLoading", false)
    },
    async markAsDone() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await ActivityService.markAsDone(this.$route.params.slug, this.activeLesson.slug)
        this.activity = response.data
      } catch (e) {
        console.log(e)
      }
      this.$store.commit("setIsLoading", false)
    },
    async getQuiz() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await CourseService.getQuiz(
            this.course.slug,
            this.activeLesson.slug
        )
        this.quiz = response.data
      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    },
    async getComments() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await CourseService.getComments(
            this.course.slug,
            this.activeLesson.slug
        )
        this.comments = response.data
      } catch (e) {
        console.error(e)
      }
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
