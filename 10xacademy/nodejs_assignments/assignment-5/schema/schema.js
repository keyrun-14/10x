const mongoose=require("mongoose");

const registration=new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true,
        unique:true
    },
    password:{
        type:String,
        required:true
    }
});

const Uploads= new mongoose.model("uploadedData",registration)
module.exports=Uploads

