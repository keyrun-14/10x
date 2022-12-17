
const mongoose=require("mongoose");
const { Schema } = mongoose;
const eachUpload= new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    location:{
        type:String,
        required:true
    },
    likes:{
        type:Number,
        required:true
    },
    description:{
        type:String
    },
    image:{
        type:String,
        required:true

    },
    user:{
        type: Schema.Types.ObjectId, 
        ref: "UploadedData"
    } 
    ,
    date:{
        type: Date,
        default: Date.now()
    }
})
const UploadDetails= new mongoose.model("mainData",eachUpload)
module.exports=UploadDetails