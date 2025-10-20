<template>
  <div class="goodlist" @scroll="onScroll">
    <Shortcut></Shortcut>
    <Header></Header>
    <div class="glmain">
      <div class="gltop">
        <div class="all">
          <div class="atxt">全部商品</div>
        </div>
        <div class="items">
          <div class="itit">分类</div>
          <div class="ichr">
            <div class="ictxt">二手手机</div>
            <div class="ictxt">手机</div>
          </div>
        </div>
      </div>
      <div class="ground">
        <div
          v-for="g in gs"
          class="gi"
          :class="{ ga: g.active }"
          @click="ground(g)"
        >
          <div class="ctxt">{{ g.text }}</div>
          <el-icon>
            <Bottom />
          </el-icon>
        </div>
      </div>
      <div class="goodsbox">
        <div
          v-for="(good, index) in lists"
          :class="{ m: (index + 1) % 5 != 0 }"
          class="gbitem"
          @click="toGoodsDetail(good.sku_id)"
        >
          <div class="imgbox">
            <img :src="good.image" alt="" srcset="" />
          </div>
          <div class="gname">
            {{ good.name }}
          </div>
          <div class="gprice">
            <div class="picin">￥</div>
            <div class="pnum">{{ good.p_price }}</div>
          </div>
          <div class="gcomment">{{ good.comment_count }}+人评论过</div>
          <div class="shopname">
            {{ good.shop_name }}
            <el-icon><ArrowRight /></el-icon>
          </div>
          <div class="catbox">
            <el-icon><ShoppingBag /></el-icon>
            <span> 加入购物清单</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import Shortcut from "@/components/Shortcut";
import Header from "@/components/home/Header.vue";
import { ref, watch } from "vue";
import { useRouter } from "vue-router";
import { getGoodsListData } from "@/network/goods.js";
import { toGoodsDetail } from "@/utils/goods.js";
const route = useRouter();

let gs = ref([
  {
    text: "综合",
    active: true,
    type: 1,
  },
  {
    text: "价格",
    active: false,
    type: 2,
  },
  {
    text: "评论数",
    active: false,
    type: 1,
  },
]);
let page = ref(1);
let keyword = ref("电脑");
let order = ref(1);
let lists = ref([]);
let cango = ref(true);
// const toGoodsDetail = (good) => {
//   let sku_id = good.sku_id;
//   console.log("跳转商品详情", good);
//   // route.push(`detail/${sku_id}`);
//   // route.push("/goods_detail/123456");
//   window.open("/detail/" + sku_id);
// };
const ground = (g) => {
  for (let i in gs.value) {
    gs.value[i].active = false;
  }
  g.active = true;
  order.value = g.type;
  lists.value = [];
  page.value = 1;
  getList();
};
const getList = () => {
  console.log("获取商品列表:", keyword.value, page.value, order.value);
  getGoodsListData(keyword.value, page.value, order.value).then((res) => {
    // console.log("商品列表数据:", res.data);
    let list = [];
    if (res.data && res.data.length > 0) {
      list = res.data.map((item) => {
        return JSON.parse(item);
      });
      lists.value = [...lists.value, ...list];
      console.log("商品列表数据:", list);
    } else {
      cango.value = false;
    }
  });
};
watch(
  () => route.currentRoute.value.params,
  (newParams, oldParams) => {
    console.log("参数变化:", newParams);
    keyword.value = newParams?.keyword ?? "电脑";
    page.value = newParams?.page ?? 1;
    order.value = newParams?.order ?? 1;
    order.value = order.value ? order.value : 1;
    console.log("ordetr:", order);
    lists.value = [];
    page.value = 1;
    getList();
  },
  { immediate: true }
);

const onScroll = (e) => {
  // console.log("scroll event:", e.target.scrollTop);
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
    getList();
  }
};
</script>
<style scoped lang="scss">
.goodlist {
  width: 100%;
  height: 100vh;
  overflow: auto;
  background-color: #f5f6fa;
  .glmain {
    width: 1200px;
    margin: auto;
    margin-top: 15px;
    min-height: 500px;
    border-radius: 16px;
    background-color: #ffffff;
    box-sizing: border-box;
    padding: 10px 15px;
    .gltop {
      width: 100%;
      padding: 10px 0;
      border-bottom: 1px solid #e0e0e0;

      .all {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        .atxt {
          color: #1a1a1a;
          font-weight: 700;
          font-size: 18px;
        }
      }
      .items {
        width: 100%;
        margin: 7px 0;
        display: flex;
        justify-content: flex-start;
        align-items: flex-start;
        position: relative;
        .itit {
          width: 84px;
          margin-right: 24px;
          font-size: 14px;
          font-weight: 700;
          color: #1a1a1a;
          line-height: 30px;
        }
        .ichr {
          width: 900px;
          height: 30px;
          //   border: 1px solid red;
          display: flex;
          justify-content: flex-start;
          align-items: flex-start;
          .ictxt {
            padding: 0 15px;
            font-size: 14px;
            color: #999;
            line-height: 30px;
          }
        }
      }
    }
    .ground {
      width: 100%;
      height: 32px;
      margin: 10px 0;
      display: flex;
      .gi {
        width: auto;
        height: 32px;
        padding: 0 20px;
        border: 1px solid #c2c4cc;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 10px;
        cursor: pointer;
      }
      .ga {
        border: 1px solid #ff0f23;
        color: #ff0f23;
        background-color: #ffebf1;
      }
    }
    .goodsbox {
      width: 100%;
      min-height: 400px;
      margin: 10px 0;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      flex-wrap: wrap;

      .gbitem {
        width: 226px;
        height: 400px;
        background-color: #fff;
        border: 1px solid #ff485e;
        border-radius: 10px;
        margin-bottom: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        box-sizing: border-box;
        padding: 6px;
        cursor: pointer;
        .imgbox {
          width: 205px;
          height: 205px;
          img {
            width: 100%;
            height: 100%;
            object-fit: cover;
          }
        }
        .gname {
          margin-top: 10px;
          width: 100%;
          // color: #ccc;
          font-size: 14px;
          display: -webkit-box;
          -webkit-line-clamp: 2; /* 限制显示的行数 */
          -webkit-box-orient: vertical;
          overflow: hidden;
          text-overflow: ellipsis;
          font-weight: 600;
        }
        .gprice {
          width: 100%;
          margin-top: 10px;
          font-size: 22px;
          color: #f30213;
          display: flex;
          font-weight: 700;
          align-items: center;
          .picin {
            font-size: 15px;
          }
        }
        .gcomment {
          width: 100%;
          color: #888b94;
          margin: 3px 0;
        }
        .shopname {
          width: 100%;
          color: #888b94;
          &:hover {
            color: #ff0f23;
          }
        }
        .catbox {
          height: 40px;
          line-height: 40px;
          margin-top: 10px;
          border-top: 1px solid #f6f6f6;
          width: 100%;
          color: #ff485e;
          text-align: center;
          font-size: 15px;
          display: flex;
          justify-content: center;
          align-items: center;
        }
      }
      .m {
        margin-right: 10px;
      }
    }
  }
}
</style>
