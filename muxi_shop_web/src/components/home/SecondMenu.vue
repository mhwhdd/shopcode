<template>
  <div class="smian">
    <template v-for="item in scdata">
      <!-- {{ item.children[0] }} -->
      <template v-for="c in item.children">
        <div v-if="c.sub_menu_type === 'channel'" class="stop">
          <div
            v-for="top in c.lists"
            @click="openurl(top.sub_menu_url)"
            class="stitem"
          >
            {{ top.sub_menu_name }}
          </div>
        </div>
        <div v-if="c.sub_menu_type !== 'channel'" class="sdetail">
          <div class="sditem">
            <div @click="openurl(c.sub_menu_url)" class="ione">
              <div class="text">{{ c.sub_menu_name }}</div>
              <div class="icon">></div>
            </div>
            <div class="smlist">
              <div
                v-for="dd in c.lists"
                @click="openurl(dd.sub_menu_url)"
                class="lchild"
              >
                {{ dd.sub_menu_name }}
              </div>
            </div>
          </div>
        </div>
      </template>
    </template>
  </div>
</template>
<script setup>
import { ref } from "vue";
// channel 上面的标题 dt 左边标题 dd 右边内容 sub_menu_id 第几行
const props = defineProps({
  scdata: {
    type: Object,
    default: () => {},
  },
  showSecondMenuIndex: {
    type: Number,
    default: 0,
  },
});
console.log(props.scdata);
const openurl = (url) => {
  // window.open(url);
  console.log("url===", url);
};
</script>
<style scoped lang="scss">
.smian {
  width: 100%;
  height: 100%;
  position: relative;
  overflow-y: auto;
  .stop {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    height: 30px;
    box-sizing: border-box;
    .stitem {
      box-sizing: border-box;
      padding: 5px 15px;
      background-color: #f5f6fa;
      color: #282829;
      font-weight: 600;
      cursor: pointer;
      border-radius: 5px;
      margin-right: 8px;
      &:hover {
        background-color: #ffebf1;
        color: #ff0f23;
      }
    }
  }
  .sdetail {
    width: 100%;
    margin-top: 10px;
    .sditem {
      width: 100%;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      margin: 5px 0;
      // border: 1px solid red;
      // background-color:
      .ione {
        width: 68px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        .text {
          color: #1a1a1a;
          font-weight: 600;
          &:hover {
            color: #ff0f23;
          }
        }
        .icon {
          color: #666666;
          &:hover {
            color: #ff0f23;
          }
        }
      }
      .smlist {
        width: 700px;
        height: 30px;
        // border: 1px solid red;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        flex-wrap: wrap;
        margin-left: 3px;
        .lchild {
          margin-right: 10px;
          color: #666666;
          cursor: pointer;
          &:hover {
            color: #ff0f23;
          }
        }
      }
    }
  }
}
</style>
