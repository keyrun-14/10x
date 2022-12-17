// let fs = require("fs");
// let data = fs.readFileSync("input.txt", 'utf-8');
// let idx = 0;
// data = data.split('\n');

// function readLine() {
//   idx++;
//   return data[idx - 1];
// }
// // // -------- Do NOT edit anything above this line ----------

// let n=parseInt(readLine());
// let arr=readLine().split(" ").map(x=>parseInt(x));
// // let arr1=[];
// // for(let i=0;i<n-1;i++)
// // {
// //     for(let j=i+1;j<n;j++)
// //     {
// //         if (arr[i] == (-1*arr[j]) )
// //         {
// //             arr1.push(arr[i])
// //         }
// //     }
    
// // }
// // if (arr1.length==0)
// // {
// //     console.log(0);
// // }
// // else{
// //     console.log(arr1)
// // }
// // let arr1=new Set(arr)
// // console.log(arr1)
// // console.log(arr1[2])
// arr.sort(function(a,b){return a-b})
// // let arr1=new Set(arr)
// // arr1=[[...arr1]]
// let arr1=arr
// console.log(arr1)
// let i=0;
// let j=arr1.length-1;
// let count=0
// while (i<j){
//     if (arr1[i]==(-1*arr[j]))
//     {
//         count=count+1;
//         i=i+1;
//         j=j-1;
//         console.log(count)
//     }
//     else{
//         j=j-1;
       
//     }
    
// }
function poR(a,b)
    {
        function sum(){
            return a+b
        }
        return 2*sum(2,3)
    }
    console.log(poR(3,4))

