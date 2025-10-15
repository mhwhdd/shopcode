<template>
  <div class="home">
    <Shortcut></Shortcut>
    <Header></Header>
    <div class="content">
      <Navigation></Navigation>
    </div>
  </div>
</template>

<script setup>
import Shortcut from "@/components/Shortcut";
import Header from "@/components/home/Header.vue";
import Navigation from "@/components/home/Navigation.vue";
</script>
<style lang="scss">
.home {
  width: 100%;
  background-color: #f5f6fa;
  min-height: 100vh;
  .content {
    width: 1200px;
    margin: 20px auto;
  }
}
</style>
