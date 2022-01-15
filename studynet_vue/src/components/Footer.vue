<template>
  <footer class="footer">
    <p class="has-text-centered">Copyright (C) {{ getCurrentYear() }}</p>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  methods: {
    getCurrentYear() {
      const date = new Date()
      return date.getUTCFullYear()
    },
  },
}
</script>
