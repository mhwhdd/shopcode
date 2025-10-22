import { request } from "./requestConfig.js";

export function loginRequest(data) {
  console.log("参数==", data);

  return request({
    url: "/user/login",
    method: "post",
    data,
  });
}
