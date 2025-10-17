<template>
  <div class="home">
    <Shortcut></Shortcut>
    <Header></Header>
    <div class="content">
      <Navigation></Navigation>
      <Banner></Banner>
    </div>
    <!-- <div class="find-goods">
      <FindGoods></FindGoods>
    </div> -->
    <div class="category">
      <div class="cateitem" v-for="(item, index) in category" :key="index">
        <div @click="toCategory(item.typeId)">
          <div
            class="category-title"
            :class="{ selected_title: item.selected }"
          >
            {{ item.title }}
          </div>
          <div
            class="category-content"
            :class="{ selected_content: item.selected }"
          >
            {{ item.content }}
          </div>
          <div class="line"></div>
        </div>
      </div>
    </div>
    <Category :categoryId="categoryId"></Category>
  </div>
</template>

<script setup>
import Shortcut from "@/components/Shortcut";
import Header from "@/components/home/Header.vue";
import Navigation from "@/components/home/Navigation.vue";
import Banner from "@/components/home/Banner.vue";
import FindGoods from "@/components/home/FindGoods.vue";
import Category from "@/components/home/Category.vue";
import { ref } from "vue";
let category = ref([
  { typeId: 1, title: "精选", content: "猜你喜欢", selected: true },
  { typeId: 2, title: "智能先锋", content: "大电器城", selected: false },
  { typeId: 3, title: "居家优品", content: "品质生活", selected: false },
  { typeId: 4, title: "超市百货", content: "百货生鲜", selected: false },
  { typeId: 5, title: "时尚达人", content: "美妆穿搭", selected: false },
  { typeId: 6, title: "进口好物", content: "京东国际", selected: false },
]);
let categoryId = ref(1);
const toCategory = (typeId) => {
  categoryId.value = typeId;
  console.log(typeId);

  for (let i in category.value) {
    category.value[i].selected = false;
    if (typeId == parseInt(i) + 1) {
      category.value[i].selected = true;
    }
  }
};
</script>
<style lang="scss">
.home {
  width: 100%;
  background-color: #f5f6fa;
  min-height: 150vh;
  overflow-y: auto;
  .content {
    width: 1200px;
    height: 500px;
    margin: 20px auto;
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
  .category {
    width: var(--content-width);
    margin: 0 auto;
    background-color: #fff;
    height: 70px;
    // text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 20px;
    box-sizing: border-box;
    .cateitem {
      width: 180px;
      height: 100%;
      // border: 1px solid red;
      margin: 0 5px;
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      .line {
        width: 2px;
        height: 30%;
        background-color: #999;
        position: absolute;
        right: 0;
        top: 35%;
      }
      &:hover {
        .category-title,
        .category-content {
          cursor: pointer;
          color: #e1251b;
        }
      }
      .category-title {
        cursor: pointer;
        color: #333333;
        font-size: 16px;
        text-align: center;
        line-height: 30px;
      }
      .category-content {
        color: #999;
        text-align: center;
      }
    }

    .selected_title {
      background-color: #e1251b;
      color: #fff !important;
      border-radius: 15px;
      padding: 0px 20px;
    }
    .selected_content {
      color: #e1251b !important;
    }
    // }
  }
}
</style>
