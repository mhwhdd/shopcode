<template>
  <div ref="scrollContainer" class="commentcon">
    <div class="allcom">买家评论({{ commentCount }}+)</div>
    <div class="commain">
      <div v-for="item in commentData" class="comitem">
        <div class="cuser">
          <div class="uava">
            <img :src="'http://' + item.user_image_url" alt="" />
          </div>
          <div class="uname">{{ item.nickname }}</div>
        </div>
        <div class="cinfo">
          <div class="ctxt">{{ item.content }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
let skuId = defineProps(["skuId"]);
import { getCommentCountData, getGoodsCommentData } from "@/network/comment.js";
const scrollContainer = ref(null);
console.log("skuId==", skuId.skuId);
let commentData = ref([]);
let commentCount = ref(0);
let page = ref(1);
let cango = ref(true);
onMounted(() => {
  // console.log(skuId);
  getCommentCountData(skuId.skuId).then((res) => {
    console.log(res);
    commentCount.value = res?.data ?? 0;
  });
  getData();
  scrollContainer.value.addEventListener("scroll", handleScroll);
});
const getData = () => {
  getGoodsCommentData(skuId.skuId, page.value).then((res) => {
    console.log(res);
    let list = res?.data ?? [];
    if (list.length <= 0) {
      cango.value = false;
    } else {
      commentData.value = [].concat(commentData.value, list);
    }
  });
};
const handleScroll = (e) => {
  const windowHeight =
    window.innerHeight ||
    document.documentElement.clientHeight ||
    document.body.clientHeight;
  const documentHeight =
    document.documentElement.scrollHeight || document.body.scrollHeight;
  // console.log(e.target.scrollTop + windowHeight - documentHeight);
  if (!cango.value) {
    return;
  }
  if (e.target.scrollTop + windowHeight >= documentHeight - 10) {
    // 当滚动到底部时，加载下一页数据
    page.value++;
    getData();
  }
};
</script>
<style scoped lang="scss">
.commentcon {
  width: 100%;
  height: 500px;
  overflow-y: auto;
  margin-top: 10px;
  .allcom {
    width: 100%;
    margin-bottom: 10px;
    color: #1a1a1a;
    font-weight: 600;
    font-size: 20px;
  }
  .commain {
    width: 100%;
    .comitem {
      width: 100%;
      margin-bottom: 20px;
      .cuser {
        width: 100%;
        height: 32px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 10px;
        .uava {
          width: 32px;
          height: 32px;
          border-radius: 50%;
          margin-right: 5px;
          img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
          }
        }
      }
      .cinfo {
        width: 100%;
        .ctxt {
          width: 100%;
          font-size: 14px;
        }
      }
    }
  }
}
</style>
