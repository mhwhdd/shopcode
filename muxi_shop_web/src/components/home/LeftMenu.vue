<template>
  <div @mouseleave="noItem()" class="leftmenu">
    <div class="mlist">
      <div
        v-for="(item, index) in mainMenu"
        class="mitem"
        @mouseover="showItem(index)"
      >
        <div v-for="(child, i) in item.children" class="child">
          <div class="ctxt">{{ child.main_menu_name }}</div>
          <div style="margin: 0 3px" v-if="i != item.children.length - 1">
            /
          </div>
        </div>
      </div>
    </div>
    <div
      v-if="isShowItem"
      class="second-item"
      @mouseover="isShowItem = true"
      @mouseleave="noItem()"
    >
      <SecondMenu
        :scdata="scdata"
        :showSecondMenuIndex="showSecondMenuIndex"
      ></SecondMenu>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { getMainMenu, getSecondMenu } from "@/network/home";
import SecondMenu from "./SecondMenu.vue";
let mainMenu = ref([]);
let isShowItem = ref(false);
let showSecondMenuIndex = ref(0);
let scdata = ref(null);
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
function categorizeDataWithMap(data) {
  const idMap = new Map();

  data.forEach((item) => {
    const id = item.sub_menu_id;
    const type = item.sub_menu_type === "channel" ? "channel" : "dt";

    if (!idMap.has(id)) {
      idMap.set(id, {
        sub_menu_id: id,
        children: new Map(),
      });
    }

    const idGroup = idMap.get(id);

    if (!idGroup.children.has(type)) {
      const newTypeGroup = {
        sub_menu_type: type,
        lists: [],
      };
      if (type === "dt") {
        newTypeGroup.sub_menu_name = item.sub_menu_name;
        newTypeGroup.sub_menu_url = item.sub_menu_url;
      }
      idGroup.children.set(type, newTypeGroup);
    }

    const typeGroup = idGroup.children.get(type);
    typeGroup.lists.push({
      sub_menu_name: item.sub_menu_name,
      sub_menu_url: item.sub_menu_url,
    });
  });

  // 转换为目标格式
  return Array.from(idMap.values()).map((group) => ({
    ...group,
    children: Array.from(group.children.values()),
  }));
}
const showItem = (index) => {
  isShowItem.value = true;
  getSecondMenu(index).then((res) => {
    let data = res.data.map((item) => {
      return JSON.parse(item);
    });
    // console.log(data);
    scdata.value = categorizeDataWithMap(data);
    // console.log(test);
  });
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
