module.exports = {
    // default 
    // entry: './path/to/my/entry/file.js'
    entry: "./src/index.js",
    watch: true,
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
            // https://stackoverflow.com/questions/33460420/babel-loader-jsx-syntaxerror-unexpected-token
            options: {
                presets: ['@babel/react']
            }
          }
        }
      ]
    }
  };