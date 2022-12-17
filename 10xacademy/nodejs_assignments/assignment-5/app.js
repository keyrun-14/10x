const express=require("express")
const app=express();
app.use(express.json());
const port=8000;
/////////////////////  cors   ///////////////////////
var cors = require('cors') 
app.use(cors())


//////////  BYCRYPT FOR PASSWORD   ////////////////////
const bcrypt = require('bcryptjs');
//////////  FETCH USER FUNCTION   ///////////////////
const fetchuser=require("./fechUser/fetchuser")
///////////  JSON WEB TOKEN ///////////////////
const secret_code="z4x5c6vt"

const jwt = require('jsonwebtoken');
////////////  BODY-PARSER  /////////////
const bodyParser=require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));
/////////////////////////  DATABASE   ////////////////////////////////
require("./db/data")
////////////////////////   SCHEMA  /////////////////////////////////
const Uploads = require("./schema/schema");

const UploadDetails=require("./schema/uploadSchema")

//////////////////////////  PATH   ///////////////////////////////
const path = require('path');
const { redirect } = require("express/lib/response");
app.set('views',path.join(__dirname,'views'));
app.set("view engine","ejs")
app.use(express.static("public")); 
/////////////////////////////////////////////////////////

const data= require("./mockdara/data.json")


//////////////////////////////////////////////////////////
app.get("/", async(req,res)=>{
    try{
         res.send(data.Data)
        // const registrations=await UploadDetails.find({})
        // res.send(registrations)
    }catch(err){
        res.send("error"+err)
    }
    // res.render("register")
    // res.send("get registration data")
})
///////////////////////////////////////////////////////////////////
app.get("/login",(req,res)=>{
    // if (req.body.email===Uploads.find({},{email:1})){
    //     console.log("get login data")
    //     res.send("hello")
    // }
    // res.send(req.body)
     res.render("login")
    // console.log("get login data")
})
///////////////////////////////////////////////////////////////////////
app.get("/register",(req,res)=>{
    // res.send("done")
     res.render("register")
})

///////////////////////////////////////////////////////////////////////
app.post("/register",async(req,res)=>{ 
    const salt=await bcrypt.genSalt(10);
    const hash=await bcrypt.hash(req.body.password,salt)

    //$2a$10$50nrNOkzC8XwNJ3fI9PIDuuskkd82jKSOE7Od5eLlATJjw9v6V44O"
    //"$2a$10$KQX7odvLIhLRp8fvxpczNOPTcb5iqBV1cCtpxWE9gLkf54NY7mLjq"
    try{   
    const uploads=  new Uploads({
        name:req.body.name,
        email:req.body.email,
        password:hash
    })
    
    const upload_temp=await uploads.save();
   
    res.send(
        {
            status:"success",
            data:upload_temp
        })
        // res.redirect("/login")
}catch(error){
    res.status(400).send(error);
}
// res.redirect("/");   
})
///////////////////////////////////////////////////////////////////////////////////////
app.post("/login",async(req,res)=>{    
   await Uploads.findOne({email:req.body.email})    
     .then((user)=> {          
            if (user === null) { 
                return res.status(400).send({ 
                    message : "User not found.",
                    status:user
                }); 
            } 
            else { 
                bcrypt.compare(req.body.password, user.password, (err, data) => {
                    //if error than throw error
                    if (err) throw err
    
                    //if both match than you can do anything
                    if (data) {
                        const payload={
                                    user :{
                                        id:user.id
                                    }
                                }
                                console.log(payload)
                                const authToken=jwt.sign(payload,secret_code)
                        return res.status(200).json({ msg: "Login success",authToken })
                    } else {
                        return res.status(401).json({ msg: "Invalid credencial" })
                    }
    
                })

                //"$2a$10$gcTpLlR9B8hh21UteRsfO.2nS24CfY.uuMlP1mriVmgQaUesZ3Tb6"
                //"$2a$10$5UXRtcsnxC5FvngMfxp.w.kIolYLkgoc2TjSYS.9QwzgZlWWTS9SK"


                // if (bcrypt.compare(req.body.password,user.password)) { 
                //     console.log(req.body.password,"   ",user.password)
                //     const payload={
                //         user :{
                //             id:user.id
                //         }
                //     }
                //     const authToken=jwt.sign(payload,secret_code)
                //     return res.status(201).send(
                //         {message : "User Logged In" ,
                //         authToken,user
                //     })
                // } 
                // else {  
                //     return res.status(400).send({ 
                //         message : "Wrong Password"
                //     }); 
                // } 
            } 
        }); 
})
///////////////////////////////////////////////////////////////////////////////////////////

app.get("/posts",fetchuser,async(req,res)=>{
    const EachUpload=await UploadDetails.find({user:req.user.id})
    res.send(EachUpload)
})

//////////////////////////////////////////////////////////////////////////////////////////////////////
app.post("/getuser",fetchuser,async(req,res)=>{
    try{
        const userId=req.user.id;
        const user=await Uploads.findById(userId).select("-password")
        res.send(user)
    }
    catch(err){res.status(500).send(err)}
})

app.post("/posts",fetchuser, async(req,res)=>{
    const {name,location,likes,description,image}=req.body
    const timeElapsed = Date.now();
    const today = new Date(timeElapsed);
    console.log("time is ",today)
    console.log(req.body)
    try{   
        const uploads_pics=  new UploadDetails({
            name,location,likes,description,image,
            date:today.toDateString(),            
            user:req.user.id
                 
        })        
        const upload_pic_temp=await uploads_pics.save();
        console.log(upload_pic_temp)
       
        res.send(
            {
                status:"post created",
                data:upload_pic_temp
            })
            // res.redirect("/login")
    }catch(error){
        res.status(400).send(error+"error");
    }

})
///////////////////////////////////////////////////////////////////////////////////////
app.put("/posts/:id",fetchuser,async(req,res)=>{
    const postId=req.params.id;
    const {title,body,image}=req.body;
  
    const newNote={}
    if (title){
        newNote.title=title}
    if(body){
        newNote.body=body
    }
    if(image){        
        newNote.image=image
        }
    
    ///find the note and update
    let note =await UploadDetails.findById(postId);
    console.log(note)
    console.log(req.user)
    if(!note){
        return res.status(401).send("post not found")
    }
    let correct_person= await Uploads.findOne({_id:note.user})

    if(!correct_person){
        return res.status(401).send("not matched || no post")
    }
    if (note.user.toString() != req.user.id){
        return res.status(401).send("not allowed make changes")
    }
    note = await UploadDetails.findByIdAndUpdate(postId,
        {$set:newNote},{new:true})
        console.log(newNote)
        res.send(note +"successfully updated")
})
/////////////////////////////////////////////////////////////////////////////////////////
app.delete("/posts/:id", fetchuser,async(req,res)=>{
    const postId=req.params.id;
    console.log(postId,"postId")
    console.log(req.user,"req.user`")
    let note =await UploadDetails.findById(postId);
    console.log(note)
    if(!note){
        return res.status(401).send("post not found")
    }
    let correct_person= await Uploads.findOne({_id:note.user})

    if(!correct_person){
        return res.status(401).send("not matched || no post")
    }
    if (note.user.toString() != req.user.id){
        
        return res.status(401).send("not allowed make changes")
    }
    UploadDetails.findByIdAndDelete(postId).then(()=> res.send({
        status:"successfully deleted"
    }))
   
})
/////////////////////////////////////////////////////////////////////////////////////////////
app.listen(port,()=>{console.log("server connected to ",port)})










// exports.login = (req, res) => {
//     let {email,password} = req.body;
//     User.findOne({email: email}).then(user => {
//        if (!user) {
//           return res.status(404).json({
//              errors: [{
//                 user: "not found"
//              }],
//           });
//        } else {
//           bcrypt.compare(password, user.password).then(isMatch => {
//              if (!isMatch) {
//                 return res.status(400).json({
//                    errors: [{
//                       password: "incorrect"
//                    }]
//                 });
//              }
//              let access_token = createJWT(
//                 user.email,
//                 user._id, 
//                 3600
//              );
//              jwt.verify(access_token, process.env.TOKEN_SECRET, (err,
//                 decoded) => {
//                 if (err) {
//                    res.status(500).json({
//                       errors: err
//                    });
//                 }
//                 if (decoded) {
//                    return res.status(200).json({
//                       success: true,
//                       token: access_token,
//                       message: user
//                    });
//                 }
//              });
//           }).catch(err => {
//              res.status(500).json({
//                 errors: err
//              });
//           });
//        }
//     }).catch(err => {
//        res.status(500).json({
//           errors: err
//        });
//     });
//  }





// app.post("/login",async(req,res)=>{
    
//     const mail= await Uploads.find({email:req.body.email,password:req.body.password})

//     if (mail===""){
//         res.send("user is not existed")
        
//     }
//  else if (req.body.email===mail[0].email  && req.body.password===mail[0].password){
//     res.send({status:"success"})
//  }
// else{
//     res.send(err+"logged in failed")
// }
 
  
// })