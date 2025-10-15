<template>
  <div class="mainheader">
    <div class="content">
      <div class="logo">
        <img src="@/assets/images/logo/logo-big.png" alt="" srcset="" />
      </div>
      <div class="serach-box">
        <div class="input-search">
          <SearchBox></SearchBox>
        </div>
      </div>
      <div class="right">
        <img src="@/assets/images/header-right.png" alt="" srcset="" />
      </div>
    </div>
  </div>
</template>
<script setup>
import SearchBox from "@/components/home/SearchBox";
</script>
<style scoped lang="scss">
.mainheader {
  width: 100%;
  .content {
    width: var(--content-width);
    margin: 0 auto;
    height: 140px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    .logo {
      img {
        width: 100px;
        height: 100px;
        object-fit: contain;
      }
    }
    .serach-box {
      width: 800px;
    }
    .right {
      //   background-color: red;
      position: absolute;
      right: 0;
      img {
        width: 200px;
        height: 140px;
        object-fit: contain;
      }
    }
  }
}
</style>
