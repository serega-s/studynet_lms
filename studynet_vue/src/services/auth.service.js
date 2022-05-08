import axios from "axios"

class AuthService {
  async login(user) {
    const response = await axios.post("token/login/", {
      username: user.username,
      password: user.password,
    })
    const token = response.data.auth_token

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token
      localStorage.setItem("token", token)
    }
  }

  async logout() {
    const response = await axios.post("token/logout/")
    axios.defaults.headers.common["Authorization"]
    localStorage.removeItem("token")
  }

  async register(user) {
    return axios.post("users/", {
      username: user.username,
      password: user.password,
    })
  }
}

export default new AuthService()
