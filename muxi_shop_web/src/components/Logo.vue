<template>
  <div class="lg">
    <img src="@/assets/images/logo/logo-big.png" alt="" />
  </div>
</template>
<script setup lang="ts">
import { ref } from "vue";
</script>
<style scoped lang="scss">
.lg {
  img {
    width: 100px;
    height: 100px;
    object-fit: contain;
  }
}
</style>
