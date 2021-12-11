<template>
  <div class="login">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Log In</h1>
        <h2 class="subtitle">Log in to continue your training</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <form @submit.prevent="submitForm">
              <div class="field">
                <label for="password">Email</label>
                <div class="control">
                  <input
                    type="email"
                    class="input"
                    name="username"
                    v-model="username"
                    placeholder="Email"
                  />
                </div>
              </div>
              <div class="field">
                <label for="password">Password</label>
                <div class="control">
                  <input
                    type="password"
                    class="input"
                    name="password"
                    v-model="password"
                    placeholder="Password"
                  />
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" :key="error">
                  {{ error }}
                </p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-dark">Sign In</button>
                </div>
              </div>
            </form>

            <hr />

            Or <router-link :to="{ name: 'SignUp' }">click here</router-link> to
            sign up!
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios"
export default {
  name: "LogIn",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    }
  },
  mounted() {
    document.title = "Log In | StudyNet"
  },
  methods: {
    submitForm() {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")

      this.errors = []

      if (!this.username) {
        this.errors.push("Username field is missing!")
      } else if (!this.password) {
        this.errors.push("Password field is missing!")
      } else if (!this.errors.length) {
        const data = {
          username: this.username,
          password: this.password,
        }

        this.$store.dispatch("login", data).then(
          () => {
            this.$router.push({ name: "MyAccount" })
          },
          (error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                )
              }
            } else if (error.message) {
              this.errors.push("Something went wrong, please try again!")
            }
          }
        )
      }
    },
  },
}
</script>
