<template>
  <div class="login">
    <div class="login-top">
      <img src="@/assets/images/logo/logo-big.png" alt="" srcset="" />
      <div class="ltxt">欢迎登录</div>
    </div>
    <div class="login-info">
      <div class="lmain">
        <div class="itit">账号登录</div>
        <div class="frombox">
          <el-form :model="userform" label-width="auto" style="width: 100%">
            <el-form-item placeholder="邮箱/账户名/手机号" label="">
              <el-input v-model="userform.username" />
            </el-form-item>
            <el-form-item placeholder="密码" label="">
              <el-input
                type="password"
                v-model="userform.password"
                show-password
              />
            </el-form-item>
            <el-form-item>
              <div
                v-if="userform.password && userform.username"
                class="loginbtn"
                @click="login"
              >
                登录
              </div>
              <div v-else class="loginbtnno">登录</div>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { loginRequest } from "@/network/user.js";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
const router = useRouter();
const store = useStore();

let userform = ref({
  username: "12@qq.com",
  password: "123456",
});
const login = () => {
  console.log(userform.value);
  loginRequest(userform.value).then((res) => {
    console.log(res);

    // return;
    if (res.status == 4000) {
      //   ElMessage("登录成功");
      ElMessage({
        message: "登录成功！",
        type: "success",
      });
      window.localStorage.setItem("token", res.data.token);
      window.localStorage.setItem("username", res.data.username);
      store.commit("setIsLogin", true);
      store.commit("setUserName", res.data.username);
      router.push("/");
    } else {
      alert(res.data);
    }
  });
};
</script>
<style scoped lang="scss">
.login {
  width: 100%;
  position: relative;
  .login-top {
    width: 100%;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    img {
      width: 70px;
      height: 70px;
      object-fit: contain;
    }
    .ltxt {
      margin-left: 5px;
      font-size: 20px;
    }
  }
  .login-info {
    margin-top: 30px;
    background-color: #e93854;
    width: 990px;
    height: 475px;
    margin: auto;
    background-image: url("@/assets/images/login/login-muxi.png");
    position: relative;
    .lmain {
      width: 320px;
      height: 400px;
      position: absolute;
      background-color: #ffffff;
      right: 100px;
      top: 30px;
      box-sizing: border-box;
      .itit {
        width: 100%;
        padding: 10px 0;
        text-align: center;
        color: #fa2c19;
        font-size: 21px;
        font-weight: 600;
        text-align: center;
      }
      .frombox {
        width: 100%;
        box-sizing: border-box;
        padding: 10px;
        .loginbtn {
          width: 100%;
          height: 40px;
          line-height: 40px;
          color: #ffffff;
          font-size: 18px;
          text-align: center;
          background-color: #fa2c19;
          border-radius: 10px;
          &:hover {
            cursor: pointer;
          }
        }
        .loginbtnno {
          width: 100%;
          height: 40px;
          line-height: 40px;
          color: #ffffff;
          font-size: 18px;
          text-align: center;
          background-color: #fd9d94;
          border-radius: 10px;

          &:hover {
            cursor: not-allowed;
          }
        }
      }
    }
  }
}
</style>
