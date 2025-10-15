<template>
  <div class="leftmenu">
    <div class="mlist">
      <div
        v-for="(item, index) in mainMenu"
        class="mitem"
        @mouseover="showItem(index)"
        @mouseleave="noItem()"
      >
        <div v-for="(child, i) in item.children" class="child">
          <div class="ctxt">{{ child.main_menu_name }}</div>
          <div style="margin: 0 3px" v-if="i != item.children.length - 1">
            /
          </div>
        </div>
      </div>
    </div>
    <div v-if="isShowItem" class="second-item">
      <SecondMenu></SecondMenu>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { getMainMenu } from "@/network/home";
import SecondMenu from "./SecondMenu.vue";
let mainMenu = ref([]);
let isShowItem = ref(false);
let showSecondMenuIndex = ref(0);
getMainMenu().then((res) => {
  let list = [];
  if (res.data) {
    list = res.data.map((item) => {
      return JSON.parse(item);
    });
    mainMenu.value = mergeMenus(list);
  }
});
function mergeMenus(menus) {
  const mergedMap = {};

  menus.forEach((menu) => {
    const id = menu.main_menu_id;
    // 如果这个id还未被记录，则初始化一个包含该id的空children数组的新对象
    if (!mergedMap[id]) {
      mergedMap[id] = {
        main_menu_id: id,
        children: [],
      };
    }
    // 将当前菜单项的名称添加到对应id的children数组中
    mergedMap[id].children.push({ main_menu_name: menu.main_menu_name });
  });

  // 将映射表对象转换为结果数组
  return Object.values(mergedMap);
}
const showItem = (index) => {
  isShowItem.value = true;
};
const noItem = () => {
  isShowItem.value = false;
};
</script>
<style scoped lang="scss">
.leftmenu {
  width: 190px;
  height: 100%;
  background-color: #ffffff;
  padding: 10px 0px;
  border-radius: 10px;
  box-sizing: border-box;
  position: relative;
  //   overflow-x: auto;
  .mlist {
    width: 100%;
    position: relative;
    .mitem {
      width: 100%;
      //   margin-bottom: 5px;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      padding: 5px 20px;
      cursor: pointer;
      box-sizing: border-box;
      //   background: red;
      &:hover {
        // color: red;
        background-color: #d9d9d9;
      }
      .child {
        // width: 100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        color: #1a1a1a;
        font-weight: 600;

        .ctxt {
          cursor: pointer;
          &:hover {
            color: #f40213;
          }
        }
      }
    }
  }
  .second-item {
    width: 900px;
    height: 100%;
    position: absolute;
    border: 1px solid #ff0f23;
    border-radius: 10px;
    top: 0;
    left: 190px;
    background-color: #ffffff;
    padding: 15px;
  }
}
</style>
