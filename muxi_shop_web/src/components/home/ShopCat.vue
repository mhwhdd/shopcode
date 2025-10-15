<template>
  <div class="shopcat">
    <el-badge :value="12" class="item">
      <el-icon color="#f40213" size="25"><ShoppingCart /></el-icon>
    </el-badge>
    <div class="stxt">我的购物车</div>
  </div>
</template>
<script setup>
import { ref } from "vue";
</script>
<style scoped lang="scss">
.shopcat {
  margin-left: 10px;
  margin-top: -30px;
  height: 35px;
  background-color: #f9f9f9;
  border: 1px solid #dfdfdf;
  display: flex;
  justify-items: center;
  justify-content: center;
  padding: 0px 20px;
  cursor: pointer;
  .item {
    // background-color: red;
    height: 20px;
    margin-top: 10px;
  }
  .stxt {
    margin-left: 22px;
    line-height: 35px;
    color: #f40213;
  }
}
</style>
