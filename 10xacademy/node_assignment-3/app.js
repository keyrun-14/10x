const express=require("express");
const bodyParser=require("body-parser");
const app= express();
const path = require('path');
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('views',path.join(__dirname,'views'));
app.set("view engine","ejs")
app.use(express.static("public")); 
const user=[];

app.get('/',function(req,res){
    res.render("table",{user})
})
app.get('/form',function(req,res){
    
    res.render("form")
})

app.post('/form', (req, res) => {
    const { Name, Email, Age, City, Profession} = req.body;
    console.log(req.body);
    user.push({ Name, Email, Age, City, Profession })
    res.redirect("/");
});
app.listen(5000,function(){
    console.log("server is running at port 5000")
})