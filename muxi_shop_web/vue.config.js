// module.exports = {
//   devServer: {
//     proxy: {
//       // 代理所有以 '/api' 开头的请求
//       "/": {
//         target: "http://127.0.0.1:8000", // 你的Django后端地址
//         changeOrigin: true, // 更改请求头中的Host，对后端透明
//         ws: false, // 确保WebSocket代理被禁用
//         pathRewrite: {
//           "/": "", // 可选：重写路径，去掉请求路径中的 '/api' 前缀
//         },
//       },
//     },
//   },
// };
