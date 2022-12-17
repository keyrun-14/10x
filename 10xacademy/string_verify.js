// let s="cat AND*dogs-awesome"
let s="a b c d-e-f%g"
// let spl_char=' -[@_!#$%^&*()<>?/\|}{~:]'
let spl_char=" `~!@#$%^&*()_+-=[]{}\|;:',./<>?"
// let spl_char=/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
let neww=""
for(let i=0;i<s.length;i++){
    if(spl_char.includes(s[i])){
        neww+="_"
    }
    else{
        neww+=s[i].toLowerCase()
    }
}
console.log(neww)
let token="umt70qfhg2e"
let new_token=""
for(let i=0;i<neww.length;i++){
    if (token.includes(neww[i])){
        new_token+="--"+neww[i]+"--"
    }
        else{
            new_token+=neww[i]
        }       
}
console.log(new_token)

// // let s="cat AND*dogs-awesome"
// let s="a b c d-e-f%g"
// // let spl_char=' -[@_!#$%^&*()<>?/\|}{~:]'
// // let spl_char=" `~!@#$%^&*()_+-=[]{}\|;:',./<>?"
// let spl_char=/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
// let neww=""
// for(let i=0;i<s.length;i++){
//     if(spl_char.test(s[i])){
//         neww+="_"
//     }
//     else{
//         neww+=s[i].toLowerCase()
//     }
// }
// console.log(neww)
// let token="umt70qfhg2e"
// let new_token=""
// for(let i=0;i<neww.length;i++){
//     if (token.test(neww[i])){
//         new_token+="--"+neww[i]+"--"
//     }
//         else{
//             new_token+=neww[i]
//         }
        
// }
// console.log(new_token)