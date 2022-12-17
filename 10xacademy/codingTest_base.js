// let fs = require("fs");
// let data = fs.readFileSync("input.txt", 'utf-8');
// let idx = 0;
// data = data.split('\n');

// function readLine() {
//   idx++;
//   return data[idx - 1];
// }
// // // -------- Do NOT edit anything above this line ----------
// let t=parseInt(readLine());
// for(let i=0;i<t;i++)
// {
//     let n=parseInt(readLine());
//     let arr=readLine().split(" ").map(x=>parseInt(x));
 
//     let sum=0;
//     for(let j=0;j<n;n++)
//     {
//         sum=sum+arr[j]
//     }
//     let avg=0;
//     console.log(sum)
//     avg=parseInt(sum/n);
  
//     let output_arr=[];
//     let item=0;
//     for(let k=0;k<n;k++)
//     {
//         if (arr[k]>avg)
//         {
//            item=avg-arr[k];
//             output_arr.push(item)
//         }
//         else{
//             output_arr.push(arr[k])
//         }
//     }
//     console.log(output_arr)
// }
// arr=[1,2,3]
// arr2=[1,2,3]
// if (arr!==arr2)
// {
//     console.log("kiran")
// }
// else{
//     console.log("10101010101")
// }