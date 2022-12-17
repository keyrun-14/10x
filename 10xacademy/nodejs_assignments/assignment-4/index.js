const express=require("express");
const app= express();
///////////////////////////////////////////////////////////////////
require("./db/data")
////////////////////////////////////////////////////////////////
const Persons = require("./model/schema")
///////////////////////////////////////////////////////////////////
const bodyParser=require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));

//////////////////////////////////////////////////////////////////
const methodOverride=require("method-override");
app.use(methodOverride("_method"));

///////////////////////////////////////////////////////////////////

app.use(express.urlencoded({ extended: true }));

app.use(express.json());
///////////////////////////////////////////////////////////////////
const path = require('path');
app.set('views',path.join(__dirname,'views'));

app.set("view engine","ejs")

app.use(express.static("public")); 

///////////////////////////////////////////////////////////////////

app.get('/',async function (req,res){
    const allUsers=await Persons.find({})
    res.render("homepage.ejs",{user:allUsers})
})
/////////////////////////////////////////////////////////////////////

app.get('/form',function(req,res){
    
    res.render("form")
});

//////////////////////////////////////////////////////////
app.post('/form', async(req, res) => {
    try{
        const registerPerson = new Persons({
            name:req.body.name,
            email:req.body.email,
            isPromoted:req.body.ispromoted
        })
        const registered = await registerPerson.save()
        // res.json(registered)
        console.log(registered)
    }catch(error){
        res.status(400).send(error);
    }
    res.redirect("/");
});
//////////////////////////////////////////////////////////////////
// app.put("/form/:id",async(req,res)=>{
//     const id=req.params.id;
//     const person=await Persons.findById(id,()=>{
//        person.isPromoted=req.body.isPromoted;
       
//     });
//     console.log(person.ispromoted)
//     // res.redirect("/");
// });
app.put("/form/:id/",async function(req,res){
    await Persons.updateOne({_id:req.params.id},[
        {$set:{
            isPromoted:
            {$not:"$isPromoted"}}}
    ])
    res.redirect("/")});

////////////////////////////////////////////////////////////////////
app.delete("/form/:id",async(req,res)=>{
    const id = req.params.id;
    await Persons.findByIdAndDelete(id)
    res.redirect("/");
});
////////////////////////////////////////////////////////////////////
app.listen(5000,function(){
    console.log("server is running 5000")
});


//////////////////////////////////////////////////////////////////////

// GET /something?color1=red&color2=blue
// app.get('/something', (req, res) => {
//     req.query.color1 === 'red'  // true
//     req.query.color2 === 'blue' // true
// })
// req.params refers to items with a ':' in the URL and req.query refers to items associated with the '?
// //route parameter in node
// var express = require('express');
// var fs  = require('fs');
// var app= express();
//  app.get('/index/profile/:id',function(req,res){
//     //  res.send('profile with id' + req.params.id)
//  });
// app.listen(3000,'127.0.0.1');
// console.log('lsitng');

//////////////////////////////////////////////////////////////////////////////////////////////