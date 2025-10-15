import axios from "axios";
import store from "@/store";
export function request(config) {
  const instance = axios.create({
    baseURL: "http://127.0.0.1:8000/",
    // baseURL:process.env.VUE_APP_BASE_URL,
    timeout: 5000,
  });

  // 请求拦截
  instance.interceptors.request.use(
    (config) => {
      // 一般来说我们会在这里边给一些实例加上token
      const token = window.localStorage.getItem("token");
      if (token) {
        // config.headers.Authorization="token";
        config.headers.Authorization = token;
      }

      // 直接放行
      return config;
    },
    (err) => {
      // 这里写一些错误的代码在这里
    }
  );

  // 响应拦截
  instance.interceptors.response.use(
    (res) => {
      if (res.data.status == false) {
        window.localStorage.setItem("token", "");
        store.commit("setIsLogin", false);
      }

      return res.data ? res.data : res;
    },
    (err) => {
      // 响应错误的在这里处理，比如404  500这些特殊的状态码
      // 咱们跳转一个特定的处理页面
    }
  );

  return instance(config);
}
