<template>
  <div class="sbox">
    <div class="content">
      <input v-model="text" class="sinp" placeholder="电脑" type="text" />
      <div @click="searchgoods" class="sicon">
        <el-icon size="20" color="#FFFFFF">
          <Search></Search>
        </el-icon>
      </div>
      <div class="words">
        <div
          v-for="item in hotwords"
          :class="{ active: item.active }"
          class="witem"
        >
          {{ item.word }}
        </div>
      </div>
    </div>
    <div class="catbox">
      <ShopCat></ShopCat>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import ShopCat from "./ShopCat.vue";
import { useRouter } from "vue-router";

const router = useRouter();
const hotwords = ref([
  {
    word: "女装",
    active: false,
  },
  {
    word: "电脑",
    active: true,
  },
  {
    word: "男装",
    active: false,
  },
  {
    word: "手机",
    active: false,
  },
  {
    word: "水果",
    active: false,
  },
]);
let text = ref("");
const searchgoods = () => {
  let kw = text.value;
  let page = 1;
  console.log("搜索商品：" + text.value);
  if (kw.trim() === "") {
    kw = "电脑";
  }
  router.push(`/goods_list/${kw}/1`);
};
</script>
<style scoped lang="scss">
.sbox {
  width: 730px;
  display: flex;
  justify-content: flex-start;
  align-items: center;

  .content {
    width: 550px;
    height: 35px;
    border: 2px solid #f30213;
    position: relative;
    margin-top: -10px;
    .words {
      width: 100%;
      height: 35px;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      position: absolute;
      bottom: -40px;
      .witem {
        color: #999999;
        margin-right: 5px;
        cursor: pointer;
        &:hover {
          color: #f30213;
        }
      }
      .active {
        color: #f30213;
      }
    }
    .sinp {
      width: 475px;
      line-height: 35px;
      height: 35px;
      margin-left: 15px;
      color: #999999;
      //   background-color: #ccd;
    }
    .sicon {
      width: 50px;
      height: 100%;
      background-color: #f30213;
      position: absolute;
      right: 0px;
      top: 0px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
    }
  }

  .catbox {
  }
}
</style>
