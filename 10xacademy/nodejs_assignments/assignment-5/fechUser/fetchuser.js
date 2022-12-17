
const jwt=require("jsonwebtoken")
const secret_code="z4x5c6vt";
const fetchuser=(req,res,next)=>{
    //getting user from the jwt token and add id to req object
    const token = req.header("authtoken");
    if(!token){
        res.status(401).send("user is not authenticated")
    }
    try{

        const data = jwt.verify(token,secret_code)
        console.log(data,"data")
    req.user=data.user
    console.log("req.user",req.user)


    next()
    }
    catch(err){res.status(401).send(err)}
    
}
module.exports=fetchuser;