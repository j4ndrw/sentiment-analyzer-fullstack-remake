module.exports = {
    configureWebpack: {
        devServer: {
            headers: { 
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
        }
    },
};