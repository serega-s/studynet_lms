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
            <form>
              <div class="field">
                <label for="password">Email</label>
                <div class="control">
                  <input
                    type="password"
                    class="input"
                    name="username"
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
                    placeholder="Password"
                  />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button class="button is-dark">Sign In</button>
                </div>
              </div>
            </form>

            <hr />

            Or <router-link to="/sign-up">click here</router-link> to sign up!
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {}
</script>
