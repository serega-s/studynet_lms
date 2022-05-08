<template>
  <h3>{{ quiz.question }}</h3>

  <div class="control">
    <div class="radio">
      <input
          v-model="selectedAnswer"
          :value="quiz.op1"
          type="radio"
      />
      {{ quiz.op1 }}
    </div>
  </div>
  <div class="control">
    <div class="radio">
      <input
          v-model="selectedAnswer"
          :value="quiz.op2"
          type="radio"
      />
      {{ quiz.op2 }}
    </div>
  </div>
  <div class="control">
    <div class="radio">
      <input
          v-model="selectedAnswer"
          :value="quiz.op3"
          type="radio"
      />
      {{ quiz.op3 }}
    </div>
  </div>
  <div class="control mt-4">
    <button class="button is-info" @click="submitQuiz">
      Submit
    </button>
  </div>
  <div v-if="quizResult === correctAnswer">
    <div class="notification is-success mt-4">
      Correct :-D
    </div>
  </div>
  <div v-else-if="quizResult === incorrectAnswer">
    <div class="notification is-danger mt-4">
      Wrong... Please try again!
    </div>
  </div>
</template>

<script>
export default {
  name: "Quiz",
  props: ["quiz"],
  data() {
    return {
      selectedAnswer: "",
      quizResult: null,
      correctAnswer: "Correct",
      incorrectAnswer: "Incorrect",
    }
  },
  methods: {
    submitQuiz() {
      this.$store.commit("setIsLoading", true)

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
      this.$store.commit("setIsLoading", false)
    },
  }
}
</script>

<style scoped>

</style>