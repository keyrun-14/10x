var http = require('http');
http.createServer(function (req, res) {
res.writeHead(200, {'Content-Type': 'text/html'});
    res.write("<h1> Hello World </h1><p> This is kiran... </p>");
    res.end();
}).listen(5000);

// var http = require("http");
// var fs = require("fs");
// http.createServer(function (req, res) {
//     if (req.url == "/") {
//       fs.readFile("index.html", function (data) {
//         res.writeHead(200, { "Content-Type": "text/html" });
//         res.write(data);
//       });
//     }
//   })
//   .listen(5000);
// console.log("ready")
