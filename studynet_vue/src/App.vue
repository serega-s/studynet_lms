<template>
  <div>
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue"
import Navbar from "@/components/Navbar.vue"
import axios from "axios"

export default {
  name: "App",
  beforeCreate() {
    this.$store.commit("initializeStore")
    const token = this.$store.state.user.token

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }
  },
  components: {
    Navbar,
    Footer,
  },
}
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
