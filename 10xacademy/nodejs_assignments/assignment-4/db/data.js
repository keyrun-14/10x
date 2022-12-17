const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1:27017/personDetails"
).then(()=>{console.log("database connection successful");
}).catch(()=>{console.log(" database connection failed")});