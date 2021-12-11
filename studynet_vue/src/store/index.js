import { createStore } from "vuex"
import AuthService from "../services/auth.service"

export default createStore({
  state: {
    user: {
      token: "",
      isAuthenticated: false,
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.user.token = localStorage.getItem("token")
        state.user.isAuthenticated = true
      } else {
        state.user.token = ""
        state.user.isAuthenticated = false
      }
    },
    setToken(state, token) {
      state.user.token = token
      state.user.isAuthenticated = true
    },
    removeToken(state) {
      state.user.token = ""
      state.user.isAuthenticated = false
    },
  },
  actions: {
    login({ commit }, user) {
      return AuthService.login(user).then(
        (token) => {
          commit("setToken", token)
          return Promise.resolve(user)
        },
        (error) => {
          commit("removeToken")
          return Promise.reject(error)
        }
      )
    },
    logout({ commit }) {
      AuthService.logout()
      commit("removeToken")
    },
    register({ commit }, user) {
      return AuthService.register(user).then(
        (response) => {
          return Promise.resolve(response.data)
        },
        (error) => {
          return Promise.reject(error)
        }
      )
    },
  },
  modules: {},
})
