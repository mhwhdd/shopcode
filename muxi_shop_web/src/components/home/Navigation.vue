<template>
  <div class="nav">
    <div class="main">
      <LeftMenu></LeftMenu>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import LeftMenu from "./LeftMenu.vue";
</script>
<style scoped lang="scss">
.nav {
  .main {
    // width: 1200px;
    height: 500px;
    // border: 1px solid red;
    margin: 0 auto;
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
}
</style>
