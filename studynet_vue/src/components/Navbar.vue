<template>
  <nav
    class="navbar is-info"
    role="navigation"
    aria-label="main navigation"
    style="min-height: 5rem;"
  >
    <div class="navbar-brand">
      <router-link class="navbar-item is-size-4" :to="{ name: 'Home' }"
        >Study Net</router-link
      >
      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbar-item"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" id="navbar-item">
      <div class="navbar-start">
        <router-link :to="{ name: 'Home' }" class="navbar-item"
          >Home</router-link
        >
        <router-link :to="{ name: 'About' }" class="navbar-item"
          >About</router-link
        >
        <router-link :to="{ name: 'Courses' }" class="navbar-item"
          >Courses</router-link
        >
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="$store.state.user.isAuthenticated">
              <router-link
                :to="{ name: 'CreateCourse' }"
                class="button is-primary"
                >Create course</router-link
              >
              <router-link :to="{ name: 'MyAccount' }" class="button is-info"
                >My Account</router-link
              >
            </template>
            <template v-else>
              <router-link :to="{ name: 'SignUp' }" class="button is-primary"
                ><strong>Sign up</strong></router-link
              >
              <router-link :to="{ name: 'LogIn' }" class="button is-light"
                ><strong>Log in</strong></router-link
              >
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
}
</script>
