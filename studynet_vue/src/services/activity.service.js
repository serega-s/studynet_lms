import axios from "axios"

class ActivityService {
  async getActiveCourses() {
    return await axios.get("activities/get_active_courses/")
  }

  async trackStarted(courseSlug, activeLessonSlug) {
    return await axios.post(`activities/track_started/${courseSlug}/${activeLessonSlug}/`)
  }

  async markAsDone(courseSlug, activeLessonSlug) {
    return await axios.post(`activities/mark_as_done/${courseSlug}/${activeLessonSlug}/`)
  }
}

export default new ActivityService()