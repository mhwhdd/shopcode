<template>
  <div class="wapper">
    <div class="header">
      <div v-if="username">{{ username }}</div>
      <div v-else @click="gologin" class="logininfo">您好，请登录</div>
      <div @click="gologin" class="reinfo">免费注册</div>
      <div class="myorder">| 我的订单</div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
const gologin = () => {
  router.push("/login");
};
let username = ref(window.localStorage.getItem("username"));
console.log("快捷登录用户名:", username.value);
</script>
<style scoped lang="scss">
.wapper {
  width: 100%;
  .header {
    margin: 0 auto;
    width: 1200px;
    height: 30px;
    background-color: #e2dbe6;
    display: flex;
    justify-content: center;
    align-items: center;
    .reinfo {
      margin: 0 5px;
    }
    div {
      cursor: pointer;
      &:hover {
        color: var(--font-red);
      }
    }
  }
}
</style>
