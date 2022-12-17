// v="kiran","kumar","tavada"
// print(v)
// hoistedVariable = 3;
// console.log(hoistedVariable); // outputs 3 even when the variable is declared after it is initialized	
// var hoistedVariable;
// let a=[1,2,3,4,5]
// console.log(a.slice(0,4))
// function reverseString(s){
//     return s.split("").reverse().join("");
// }
// a=reverseString("Hello");//"olleH"
// console.log(a)
// let a=[1,2,3,4]
// let b=a
// a[3]=9
// console.log(a,b)
// function doSomething() {
//     console.log(this);
//   }
     
//   doSomething();

// function saySomething(message){
//     return this.name + " is " + message;
//   }        
//   var person4 = {name:  "John"};
//  console.log(saySomething.apply(person4, ["awesome","kiran"])) 
// let a= "2"*5
// console.log(a)

// let a=[1,2,3,4]
// d={}
// for (let i of a){
//     if( i in d){
//         d[i]=d[i]+1
//     }
//     else{
//         d[i]=1
//     }
// }
// console.log(d)
// for(let x in d){
//     console.log(x,d[x])
// }
// let a=[1,2,3,4,5,6]
// x=4
// let b= a.filter(item=>(x==item))
// console.log(b)
// let myarray = [
//     {
//       name: "John",
//       city: "london",
//       dept: "computer",
//       salary: 1000,
//     },
//     {
//       name: "bella",
//       city: "new york",
//       dept: "fianance",
//       salary: 1000,
//     },
//     {
//       name: "justine",
//       city: "paris",
//       dept: "computer",
//       salary: 1000,
//     },
//   ];
//   console.log("myarray : ", myarray);
//   // ----------------------------------
//   // map
//   let mapArray = myarray.map(function (item) {
//     return item.name;
//   });
//   console.log("mapArray : ", mapArray);
//   // ----------------------------------
//   //filter
//   let filterArray = myarray.filter(function (item) {
//     if (item.dept == "computer") {
//       return true;
//     } else {
//       return false;
//     }
//   });
//   console.log("filterArray : ", filterArray);
//   // ----------------------------------
//   //reduce
//   // 1.
//   let reduceArray1 = myarray.reduce(function (acc, item) {
//     return acc + item.salary;
//   }, 0);
//   console.log("reduceArray1 : ", reduceArray1);
//   // ------
//   // 2.
//   let reduceArray2 = myarray.reduce(
//     function (acc, item) {
//       if (item.dept == "computer") {
//         acc.com.push(item.name);
//       } else {
//         acc.finance.push(item.name);
//       }
//       return acc;
//     },
//     { com: [], finance: [] }
//   );
//   console.log("reduceArray2 : ", reduceArray2);
