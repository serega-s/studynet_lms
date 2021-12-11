<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">My Account</h1>
      </div>
    </div>

    <section class="section">
      <button class="button is-warning is-outline" @click="logout()">
        Log out
      </button>
    </section>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "MyAccount",
  mounted() {
    document.title = "My Account | StudyNet"
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(
        () => {
          this.$router.push({ name: "LogIn" })
        },
        (error) => {
          console.log(error.response)
        }
      )
    },
  },
}
</script>

<style></style>
