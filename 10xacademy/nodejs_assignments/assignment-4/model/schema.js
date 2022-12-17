const mongoose = require("mongoose");
const personSchema = new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true,
        unique:true
    },
    isPromoted:{
        type:Boolean||Object,
        default:null
    }
})
// collections
const Persons = new mongoose.model("PersonDetails",personSchema);
module.exports = Persons