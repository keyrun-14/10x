let fs = require("fs");
let data = fs.readFileSync("input.txt", 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// // -------- Do NOT edit anything above this line ----------
// let n=parseInt(readLine());
// if(1<=n<= 1000000)
// {
//     let a=readLine().split(" ").map(x=>parseInt(x)).slice(0,n);
//     let product=0;
//     let i=0;
//     let j=1;
//     while (i<n-1)
//     {  
//         while (j<n){
//             product=product+Math.abs(a[i]*a[j])
        
//             j=j+1
            
//         }
//         i=i+1
//         j=i+1
//     }console.log(product);
// }

let n=parseInt(readLine());
let a=readLine().split(" ").map(x=>parseInt(x)).slice(0,n);
let product=0;
let sum=0;
if (n==1){
  console.log(a[0])
}else{
  for (let i=0;i<n;i++){
    product=product+Math.abs(sum*a[i])
    sum=sum+Math.abs(a[i])    
  }
  console.log(product);
}


  
// function product(n,arr,sqOfArr,sumOfArr){
//   for(i=0;i<n;i++){
//       if(arr[i]<0){
//           arr[i]=arr[i]*(-1)
//       }
//       sqOfArr=sqOfArr+arr[i]
//   }
//   sqOfArr=sqOfArr*sqOfArr
//   for(i=0;i<n;i++){
//       sumOfArr=sumOfArr+(arr[i]*arr[i])
//   }
//   result=(sqOfArr-sumOfArr)/2
//   return parseInt(result)
// }
// let n=parseInt(readLine());
// let arr=readLine().split(" ").map((x)=>parseInt(x))
// console.log(product(n,arr,0,0))


