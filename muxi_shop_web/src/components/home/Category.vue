<template>
  <div class="categorycon">
    <div
      v-for="(item, index) in goods"
      :class="{ m: (index + 1) % 5 != 0 }"
      class="cate-item"
      @click="toGoodsDetail(item.target_url)"
    >
      <div class="catdet">
        <div class="imgbox">
          <img :src="item.image" alt="" srcset="" />
        </div>
        <div class="cattxt">{{ item.name }}</div>
      </div>

      <div class="catpri">
        <div class="picin">￥</div>
        <div class="pnum">{{ item.jd_price }}</div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, watch } from "vue";
import { getCategoryGoods } from "@/network/home.js";
import { toGoodsDetail } from "@/utils/goods.js";

const props = defineProps({
  categoryId: {
    type: Number,
    default: 0,
  },
});
let goods = ref([]);
// 用来存储现在是多少页
let page = ref(1);
let cango = ref(true);
const getCategoryGoodsData = (c, p) => {
  getCategoryGoods(c, p).then((res) => {
    let data = res.data;
    let list = [];
    if (data.length > 0) {
      list = data.map((item) => {
        return JSON.parse(item);
      });
      goods.value = [...goods.value, ...list];
      console.log("goods===", goods.value);
      page.value++;
    } else {
      cango.value = false;
    }
  });
};

const resetAndFetchData = () => {
  goods.value = [];
  page.value = 1;
  getCategoryGoodsData(props.categoryId, page.value);
};

onMounted(() => {
  resetAndFetchData();
});

watch(
  () => props.categoryId,
  () => {
    page.value = 1;
    cango.value = true;
    resetAndFetchData();
  }
);
window.addEventListener("scroll", () => {
  const scrollTop =
    window.pageYOffset ||
    document.documentElement.scrollTop ||
    document.body.scrollTop ||
    0;
  const windowHeight =
    window.innerHeight ||
    document.documentElement.clientHeight ||
    document.body.clientHeight;
  const documentHeight =
    document.documentElement.scrollHeight || document.body.scrollHeight;
  if (!cango.value) {
    return;
  }
  if (scrollTop + windowHeight >= documentHeight - 10) {
    // 当滚动到底部时，加载下一页数据
    getCategoryGoodsData(props.categoryId, page.value);
  }
});
</script>
<style scoped lang="scss">
.categorycon {
  width: 1200px;
  margin: auto;
  // height: 100px;
  margin-top: 10px;
  // background-color: red;
  // width: 120px;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  .cate-item {
    width: 232px;
    height: 350px;
    background-color: #fff;
    border-radius: 10px;
    margin-bottom: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    box-sizing: border-box;
    padding: 18px;
    .catdet {
      width: 190px;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      cursor: pointer;
      // position: relative;
      &:hover .cattxt {
        color: #f40213;
      }
      &:hover .imgbox::before {
        content: ""; // 必须有内容才能显示
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(255, 255, 255, 0.2); // 半透明黑色蒙层
        z-index: 1; // 确保蒙层在图片之上
      }
      .imgbox {
        width: 190px;
        height: 190px;
        position: relative;
        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          position: relative;
        }
      }
      .cattxt {
        margin-top: 15px;
        width: 100%;
        color: #666666;
        font-size: 14px;
        display: -webkit-box;
        -webkit-line-clamp: 2; /* 限制显示的行数 */
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }
    .catpri {
      width: 100%;
      margin-top: 20px;
      font-size: 22px;
      color: #f30213;
      display: flex;
      font-weight: 700;
      align-items: center;
      .picin {
        font-size: 15px;
      }
      .pnum {
      }
    }
  }
  .m {
    margin-right: 10px;
  }
}
</style>
