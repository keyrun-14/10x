
let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ---------- 
// let t=parseInt(readLine());
// if(t>0)
// {
//     for(let i=0;i<t;i++)
//     {
//         let b=parseInt(readLine())
//         if(b>0)
//         {
//             let a=readLine().split(" ").map(x => parseInt(x));//.slice(0,b);
//             //a.sort();
//             a.sort(function(a, b){return a-b});
//             //console.log(a)
//             let left=0
//             for(let i=0;i<parseInt(b/2);i++){
//                 left=left+a[i]
//             }
//             let right=0
//             for(let i=parseInt(b/2);i<b;i++){
//                 right=right+a[i]
//             }
//             console.log(right-left)

//         }else{
//             console.log(0)
//         }
// }
// }else{
//     console.log(0)
// }

/////////////////////////////////////////////
// let t=parseInt(readLine());
// for(let i=0;i<t;i++)
// {
//     let n=parseInt(readLine());
//     a = readLine().split(" ").map(x => parseInt(x));
//     a.sort(function(a, b){return a-b});;
//     let sum=0;
//     let res=parseInt(n/2);
//     let i=0;
//     while(i<res)
//         {
//             sum=sum+a[n-i-1]-a[i];
//             i++;
//         }
//     if (n%2!=0){
//         sum=sum+a[i]
//         console.log(sum);
//     }else{
//         console.log(sum);
//     } 
// }
let num=parseInt(readLine());
if (num>0)
{
    while(num > 0)
    {        
        let arrLength = parseInt(readLine());
        if (arrLength > 0)
        {
            let arr = readLine().split(' ');
            arr.sort(function(a, b){return a - b});
            //console.log(arr);        
            let left = parseInt(arr.length/2);
            let leftSum = 0;
            let rigthSum = 0;
            for(let i = 0; i < left; i++)
            {
                leftSum += parseInt(arr[i]);
                // console.log(leftSum);
            }
            for(let j = left; j <arr.length; j++)
            {
                rigthSum += parseInt(arr[j]);
                // console.log(rigthSum);
            }
            console.log((rigthSum-leftSum));
            //console.log(rigthSum);
            //console.log((leftSum));
        }
        else
        {
            console.log(0);
        }
        num--;
    }
}else{ 
    console.log(0)
}