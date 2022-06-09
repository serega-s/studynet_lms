import { createRouter, createWebHistory } from "vue-router"
import About from "../views/About.vue"
import Home from "../views/Home.vue"
import Courses from "../views/Courses.vue"
import SignUp from "../views/SignUp.vue"
import LogIn from "../views/LogIn.vue"
import Course from "../views/Course.vue"
import MyAccount from "../views/dasboard/MyAccount.vue"
import Author from "../views/Author.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/dashboard/my-account",
    name: "MyAccount",
    component: MyAccount,
  },
  {
    path: "/courses",
    name: "Courses",
    component: Courses,
  },
  {
    path: "/courses/:slug",
    name: "Course",
    component: Course,
  },
  {
    path: "/authors/:id",
    name: "Author",
    component: Author,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
