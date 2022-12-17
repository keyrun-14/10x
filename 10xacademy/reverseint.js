let l=-120
let s=0
if (l<0){
    a=-1*l
}else{
    a=l
}
do{
    reminder=a%10
    s=s*10+reminder
    a=parseInt(a/10)
}while (a>0);
if (l<0){
    s=s*-1
}else{
    s=s
}
console.log(s)

// else{
//     do{
//         reminder=a%10
//         s=s*10+reminder
//         a=parseInt(a/10)
//     }while (a>0);
//     console.log(s)
// }

