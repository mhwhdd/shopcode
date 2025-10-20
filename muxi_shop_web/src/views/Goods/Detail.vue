<template>
  <div class="detail">
    <Shortcut></Shortcut>
    <Header></Header>
    <div v-if="good" class="dmain">
      <div class="dmleft">
        <div class="imgbox">
          <div class="imin">
            <img :src="good.image" alt="" srcset="" />
          </div>
          <div class="ibig">
            <img :src="good.image" alt="" srcset="" />
          </div>
        </div>
        <div class="dinfo">
          <div class="dtit">
            <div
              v-for="t in tits"
              class="dttiem"
              :class="{ active: t.active }"
              @click="changetit(t)"
            >
              {{ t.text }}
              <div v-if="t.active" class="dline"></div>
            </div>
          </div>
          <div class="aline"></div>
          <Comment :skuId="skuId"></Comment>
        </div>
      </div>
      <div class="dmright">
        <div class="desc">{{ good.name }}</div>
        <div class="dprice">￥{{ good.p_price }}</div>
        <div class="getbox">
          <div class="cnum">
            <el-input-number
              v-model="num"
              @change="handleChange"
              :min="1"
              :max="10"
              label=""
              class="inum"
            ></el-input-number>
          </div>
          <div class="addcart">加入购物车</div>
          <div class="gobuy">立即购买</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import Shortcut from "@/components/Shortcut.vue";
import Header from "@/components/home/Header.vue";
import Comment from "@/components/GoodsDetail/Comment";

import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { getGoodsDetail } from "@/network/goods.js";

let skuId = ref("");
const route = useRoute();
let good = ref(null);
let num = ref(1);

let tits = ref([
  {
    text: "大家评",
    active: true,
  },
  {
    text: "店铺",
    active: false,
  },
  {
    text: "商品详情",
    active: false,
  },
  {
    text: "售后保障",
    active: false,
  },
  {
    text: "推荐",
    active: false,
  },
]);
const handleChange = (value) => {
  num.value = value;
};
onMounted(() => {
  skuId.value = route.params.sku_id;
  getGoodsDetail(skuId.value).then((res) => {
    good.value = res.data;
    console.log("商品详情数据:", good.value);
  });
});
const changetit = (t) => {
  tits.value.forEach((item) => {
    item.active = false;
  });
  t.active = true;
};
</script>
<style scoped lang="scss">
.detail {
  width: 100%;
  height: 100vh;
  margin: auto;
  overflow-y: auto;
  background-color: #f5f6fa;
  .dmain {
    width: 1200px;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    .dmleft {
      width: 656px;
      .imgbox {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        .imin {
          width: 88px;
          height: 88px;
          cursor: pointer;
          img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 10px;
          }
        }
        .ibig {
          width: 552px;
          height: 552px;
          cursor: pointer;
          img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 10px;
          }
        }
      }
      .dinfo {
        width: 100%;
        background-color: #ffffff;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 12px;
        position: relative;
        .dtit {
          width: 100%;
          display: flex;
          align-items: center;
          height: 50px;
          .dttiem {
            color: #1a1a1a;
            font-size: 16px;
            font-weight: 600;
            line-height: 50px;
            margin-right: 15px;
            cursor: pointer;
            position: relative;
            z-index: 1;
            .dline {
              width: 100%;
              // border: 2px ;
              height: 2px;
              background-color: #ff0f23;
              position: absolute;
              bottom: 0;
            }
          }
          .active {
            color: #ff0f23;
          }
        }
        .aline {
          width: 100%;
          height: 2px;
          background-color: #dadce0;
          position: absolute;
          top: 60px;
          left: 0;
        }
      }
    }
    .dmright {
      width: 510px;
      background-color: #ffffff;
      position: relative;
      border-radius: 10px;
      min-height: 600px;
      padding: 10px;
      .desc {
        width: 100%;
        font-size: 20px;
        color: #1a1a1a;
        font-weight: 600;
        line-height: 26px;
      }
      .dprice {
        width: 100%;
        font-size: 24px;
        color: #ff0f23;
        font-weight: 700;
        margin-top: 15px;
      }
      .getbox {
        width: 100%;
        // position: absolute;
        width: 100%;
        height: 40px;
        // background-color: red;
        margin-top: 30px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        .cnum {
          height: 100%;
          width: 130px;
          .inum {
            width: 130px;
            height: 100%;
          }
        }
        .addcart {
          height: 100%;
          padding: 0 30px;
          background-color: #ff475d;
          cursor: pointer;
          text-align: center;
          line-height: 40px;
          color: #ffffff;
          font-size: 21px;
          border-radius: 8px;
        }
        .gobuy {
          height: 100%;
          padding: 0 30px;
          background-color: #ff475d;
          cursor: pointer;
          text-align: center;
          line-height: 40px;
          color: #ffffff;
          font-size: 21px;
          border-radius: 8px;
        }
      }
      //   height: ;
    }
  }
}
</style>
