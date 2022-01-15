<template>
  <div class="signup">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign Up</h1>
        <h2 class="subtitle">Sign up to use our learning platform</h2>
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
              <div class="field">
                <label for="password">Repeat Password</label>
                <div class="control">
                  <input
                    type="password"
                    class="input"
                    name="password"
                    v-model="password2"
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
                  <button class="button is-dark">Sign Up</button>
                </div>
              </div>
            </form>
            <hr />

            Or <router-link :to="{ name: 'LogIn' }">click here</router-link> to
            log in!
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios"
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    }
  },
  mounted() {
    document.title = "Sign Up | StudyNet"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      this.errors = []

      if (!this.username) {
        this.errors.push("Username field is missing!")
      } else if (!this.password || this.password.length < 8) {
        this.errors.push("Password must contain at least 8 characters")
      } else if (this.password !== this.password2) {
        this.errors.push("Passwords don't match!")
      } else if (!this.errors.length) {
        const data = {
          username: this.username,
          password: this.password,
        }

        this.$store.dispatch("register", data).then(
          () => {
            this.$router.push({ name: "LogIn" })
          },
          (error) => {
            console.log(error.response)

            if (error.response.data) {
              for (const property in error.response.data) {
                this.errors.push(`${error.response.data[property]}`)
              }
            } else {
              this.errors.push("Unable to sign up with bad credentials.")
            }
          }
        )
      }
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
