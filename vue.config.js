module.exports = {
    configureWebpack: {
        devServer: {
            headers: { "Access-Control-Allow-Origin": "*" },
            proxy: {
                "/predict": {
                    target: "http://localhost:5000/predict",
                    secure: false,
                    changeOrigin: true
                }
            }
        }
    },
};