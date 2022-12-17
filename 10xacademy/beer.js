// // ## Calculate the liquor consumption in an order
// // ### Description
// // Pubs/Bars wants to buy liquor from distributors online, you need to write a function that will calculate total liquor for the order in HL (hectolitre) in a year based on user preferences.
// // [Video Description](https://youtu.be/7HjGf2eYSO4)

// // ### Rules
// // - Packaging type for the order. If the user selects a bottle, a bottle can contain 330 milliliters.
// // - Order frequency will be given in a number of weeks.
// // - Quantity per order will be given in liters.

// // ### Calculations

// // - You need to calculate the total volume of the order in a year.
// // - You need to calculate the number of units required per order based on the selection of the packaging option.
// // - You also need to return the selection of packaging option.

// ///#### Input
// ```
// // Constants requried for calculations
// const packaging = [
//     { id: 1, title: "kegs", size: 30000 }, // size in milliliter
//     { id: 2, title: "bottle", size: 330 }, // size in milliliter
//     { id: 3, title: "can", size: 300 }, // size in milliliter
//     { id: 4, title: "container", size: 1000000 }, // size in milliliter
// ];
// ```
// ```
// // Input for your function
// {
//     id: 1,
//     title: "Beer for a pub",
//     packaging: 2, // id of the packaging
//     orderFrequency: 3, // order frequency in weeks
//     quantityPerOrder: 1000, // quantity per order in litres
//     createdAt: 1589265720000,
// }
// ```
// /// Output
// ```
// {
//   totalVolumeInYear: 12,
//   packaging: "bottles",
//   unitsPerOrder: 24,
// }
// ```



// let fs = require("fs");
// let data = fs.readFileSync("input.txt", 'utf-8');
// let idx = 0;
// data = data.split('\n');

// function readLine() {
//   idx++;
//   return data[idx - 1];
// }
// // // -------- Do NOT edit anything above this line ----------

function calLiquor({id, title, packaging, orderFrequency, quantityPerOrder, createdAt}){
    const collection = [
        { id: 1, title: "kegs", size: 30000 }, // size in milliliter
        { id: 2, title: "bottle", size: 330 }, // size in milliliter
        { id: 3, title: "can", size: 300 }, // size in milliliter
        { id: 4, title: "container", size: 1000000 }, // size in milliliter
    ];
    if (packaging==1){
        id = packaging
        packaging = collection[id - 1].title
    }
    else if (packaging == 2) {
        id=packaging
        packaging = collection[id-1].title
    }
    else if (packaging == 3) {
        id = packaging
        packaging = collection[id - 1].title
    }
    else if (packaging == 4) {
        id = packaging
        packaging = collection[id - 1].title
    }
    console.log(id, title, packaging, orderFrequency, quantityPerOrder, createdAt)
    return
}
calLiquor(
    {
        id: 1,
        title: "Beer for a pub",
        packaging: 2, // id of the packaging
        orderFrequency: 3, // order frequency in weeks
        quantityPerOrder: 1000, // quantity per order in litres
        createdAt: Date.now(),
    }
)

var date = new Date("12/31/2020");
var milliseconds = date.getTime();
console.log(milliseconds);