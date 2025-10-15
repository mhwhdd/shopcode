import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "@/assets/css/config.css";
// 引入iconfont样式
// import "@/assets/iconfont/iconfont.css";
// 引入element-plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
// 滚动插件的引入
import vue3SeamlessScroll from "vue3-seamless-scroll";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

const app = createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}
app
  .use(store)
  .use(router)
  .use(ElementPlus)
  .use(vue3SeamlessScroll)
  .mount("#app");
