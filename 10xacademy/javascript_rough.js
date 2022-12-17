// arr=["fiat",500,"audi",700,"benz",900]
// let person = new Object();
//     for(let i=0;i<arr.length -1;i++){
//         if(i%2===0){
//             person[arr[i]] = arr[i+1]
//         }
//     }
//     console.log(person) 

// var arr = [1,3,4,6,7] 
// var removed = arr.splice(3,1);
// console.log(arr)
// function doSomething(){
//     x = 33;
    
//     var x;
//     console.log(x);
//   }
// doSomething();  
// let x=3;
// let y="k";
// console.log(x-y)
// var x = NaN;
// var y = 23;
        
// if(x) { console.log(x) }   // The code inside this block will not run since the value of x is 0(Falsy)  
        
// if(y) { console.log(y) }    // The code inside this block will run since the value of y is 23 (Truthy)
// var x = 220;
// var y = "Hello";
// var z = undefined;
        
// // x | | y    // Returns 220 since the first value is truthy
        
// // x | | z   // Returns 220 since the first value is truthy
        
// // x && y    // Returns "Hello" since both the values are truthy
        
// // y && z   // Returns undefined since the second value is falsy
        
// if( x && y ){ 
//   console.log("Code runs" ); // This block runs because x && y returns "Hello" (Truthy)
// }   
        
// if( x || z ){
//   console.log("Code runs");  // This block runs because x || y returns 220(Truthy)
// }
// console.log(x && y)

// function doSomething() {
//   console.log(this);
// }
        
// doSomething();
// function multiply(a,b){
//   return a*b;
// }

// function currying(fn){
//   return function(a){
//     return function(b){
//       return fn(a,b);
//     }
//   }
// }

// var curriedMultiply = currying(multiply);

// console.log(multiply(4, 3)); // Returns 12

// console.log(curriedMultiply(4)(3)); 
// function name(){
//   console.log("kiran")
// }

// function nameKind(name)
//   {
//     console.log("hello")
//   name()
//   }
// nameKind(name)

// console.log(a)
// a=5;
// var a;

// {let a;
// a=5;
// console.log(a)}


const getData = async() => {
  var y = await "Hello World";
  console.log(y);
}

console.log(1);
getData();
console.log(2);

