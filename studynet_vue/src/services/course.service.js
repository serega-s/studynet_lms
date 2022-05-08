import axios from "axios"

class CourseService {
  async getCategories() {
    return await axios.get("courses/get-categories/")
  }

  async getCourses(url) {
    return await axios.get(url)
  }

  async getComments(course_slug, activeLesson_slug) {
    return await axios.get(
        `courses/${course_slug}/${activeLesson_slug}/get-comments/`
    )
  }

  async getQuiz(course_slug, activeLesson_slug) {
    return await axios.get(
        `courses/${course_slug}/${activeLesson_slug}/get-quiz/`
    )
  }

  async submitComment(course_slug, activeLesson_slug, data) {
    return await axios.post(
        `courses/${course_slug}/${activeLesson_slug}/`,
        data
    )
  }

  async getCoursesLessonsData(slug) {
    return await axios.get(`courses/${slug}/`)
  }
}

export default new CourseService()
