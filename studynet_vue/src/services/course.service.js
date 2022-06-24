import axios from "axios"

class CourseService {
  async getCategories() {
    return await axios.get("courses/get-categories/")
  }

  async createCourse(data) {
    return await axios.post("courses/create/", data)
  }

  async getCourses(url) {
    return await axios.get(url)
  }

  async getComments(courseSlug, activeLessonSlug) {
    return await axios.get(
      `courses/${courseSlug}/${activeLessonSlug}/get-comments/`
    )
  }

  async getQuiz(courseSlug, activeLessonSlug) {
    return await axios.get(
      `courses/${courseSlug}/${activeLessonSlug}/get-quiz/`
    )
  }

  async submitComment(courseSlug, activeLessonSlug, data) {
    return await axios.post(`courses/${courseSlug}/${activeLessonSlug}/`, data)
  }

  async getCoursesLessonsData(slug) {
    return await axios.get(`courses/${slug}/`)
  }
}

export default new CourseService()
