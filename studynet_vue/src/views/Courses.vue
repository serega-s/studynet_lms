<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Courses</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-2">
            <aside class="menu">
              <p class="menu-label">Categories</p>

              <ul class="menu-list">
                <li>
                  <a
                    :class="{ 'is-active': !activeCategory }"
                    @click="setActiveCategory(null)"
                    >All courses</a
                  >
                </li>
                <li
                  v-for="category in categories"
                  :key="category.id"
                  @click="setActiveCategory(category)"
                >
                  <a>{{ category.title }}</a>
                </li>
              </ul>
            </aside>
          </div>

          <div class="column is-10">
            <div class="columns is-multiline">
              <div
                class="column is-4"
                v-for="course in courses"
                :key="course.id"
              >
                <CourseItem :course="course" />
              </div>
            </div>

            <div class="column is-12">
              <nav class="pagination">
                <a class="pagination-previous">Previous</a>
                <a class="pagination-next">Next</a>

                <ul class="pagination-list">
                  <li>
                    <a class="pagination-link is-current">1</a>
                  </li>
                  <li>
                    <a class="pagination-link">2</a>
                  </li>
                  <li>
                    <a class="pagination-link">3</a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios"
import CourseItem from "../components/CourseItem.vue"
export default {
  components: { CourseItem },
  name: "Courses",
  data() {
    return {
      courses: [],
      categories: [],
      activeCategory: null,
    }
  },
  async mounted() {
    document.title = 'Courses | StudyNet'
    
    await axios
      .get("/api/v1/courses/get-categories/")
      .then((response) => {
        this.categories = response.data
      })
      .catch((error) => {
        console.log(error.response)
      })

    this.getCourses()

    
  },
  methods: {
    setActiveCategory(category) {
      this.activeCategory = category
      this.getCourses()
    },
    getCourses() {
      let url = "/api/v1/courses/"

      if (this.activeCategory) {
        url += "?category_id=" + this.activeCategory.id
      }
      axios
        .get(url)
        .then((response) => {
          this.courses = response.data
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
  },
}
</script>
