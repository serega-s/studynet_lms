import axios from "axios"

class CourseService {
  getFrontpageCourses() {
    const response = axios.get("/api/v1/courses/get-frontpage-courses/")

    return response
  }
  getCategories() {
    const response = axios.get("/api/v1/courses/get-categories/")

    return response
  }
  getCourses(url) {
    const response = axios.get(url)

    return response
  }
  getComents(course_slug, activeLesson_slug) {
    const response = axios.get(
      `/api/v1/courses/${course_slug}/${activeLesson_slug}/get-comments/`
    )

    return response
  }
  getQuiz(course_slug, activeLesson_slug) {
    const response = axios.get(
      `/api/v1/courses/${course_slug}/${activeLesson_slug}/get-quiz/`
    )

    return response
  }
  submitComment(course_slug, activeLesson_slug, data) {
    const response = axios.post(
      `/api/v1/courses/${course_slug}/${activeLesson_slug}/`,
      data
    )

    return response
  }
  getCoursesLessonsData(slug) {
    const response = axios.get(`/api/v1/courses/${slug}/`)

    return response
  }
}

export default new CourseService()
