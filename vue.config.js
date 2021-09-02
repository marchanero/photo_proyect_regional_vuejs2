module.exports = {
  devServer: {
    compress:true,
    disableHostCheck: true,
    host: '0.0.0.0',
    port: 8000,
    proxy: 'https://api.emosys.site/',
    // proxy: {
    //   '/V1': {
    //       target: 'http://localhost:8888',
    //       changeOrigin: true,
    //       pathRewrite: {
    //           '^/V1': ''
    //       }
    //   },
    //   '/V2': {
    //       target: 'https://loclhost:4437',
    //       changeOrigin: true,
    //       pathRewrite: {
    //           '^/V2': ''
    //       }
    //   }
    // }
  }

}
  