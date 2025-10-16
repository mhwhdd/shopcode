<template>
  <div class="banner">
    <el-carousel class="bannermain">
      <el-carousel-item
        v-for="item in lists"
        :key="item"
        indicator-position="outside"
        type="card"
      >
        <!-- <h3 class="small justify-center" text="2xl">{{ item }}</h3> -->
        <img :src="item" alt="" srcset="" />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>
<script setup>
import { ref } from "vue";
import b1 from "@/assets/images/banner/banner1.png";
import b2 from "@/assets/images/banner/banner2.png";
import b3 from "@/assets/images/banner/banner3.png";
import b4 from "@/assets/images/banner/banner4.png";
import b5 from "@/assets/images/banner/banner5.png";
import b6 from "@/assets/images/banner/banner6.png";
let lists = ref([b1, b2, b3, b4, b5, b6]);
</script>
<style scoped lang="scss">
.banner {
  width: 710px;
  height: 100%;
  margin: 0 10px;
  border-radius: 12px;
  border-radius: 12px;
  background-image: url("@/assets/images/banner/b1.jpeg");
  background-size: cover;
  .bannermain {
    width: 100%;
    height: 300px;
    // background-color: red;
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}
</style>
