let array1 = [65,83,"Meredian",26,true];
let array2 = [20,"Mean"];

// array size
let array1length = array1.length;
console.log("The size of array1 is:", array1length);

let array2length = array2.length;
console.log("The size of array2 is:", array2length);

// Adding and removing elements
array1.pop();
console.log("\nThe size of array after pop is:",array1.length);
console.log(array1);

array1.push(3);
console.log("\nThe size of array after pop is:",array1.length);
console.log(array1);

// array slicing
var slicedarray = array1.slice(1,3)
console.log("\nThe size of array after pop is:",array1.length);
console.log(slicedarray);

// Add another array to existing array
let newArray = [120, 130, 140];
array2 = array2.concat(newArray);
console.log("\nArray after adding another array:", array2);

// Replace old array with new array
let replacementArray = [200, 300, 400];
array2 = replacementArray;
console.log("\nArray2 after replacement:", array2);

// Count of two arrays
let anotherArray = [5, 15, 25, 35];
let combinedCount = array2.length + anotherArray.length;
console.log("\nCombined count of two arrays:", combinedCount);

// Index of 2 array elements
// let index1 = array2.indexOf(110);
let index2 = array2.indexOf(300);
// console.log("\nIndex of element 110 is:", index1);
console.log("\nIndex of element 300 is:", index2);

// boolean(is true)
let ispresent = array2.includes(3);
console.log("\n",ispresent);

// sorting elements in an array
let sortedarray = array2.sort();
console.log("\nArray after sorting elements is:",sortedarray);

// join
let joiningarray = array2.join("@");
console.log("\nArray after joining elements:",joiningarray);

let array = [1,2,3];
let slicedArray = array.slice(1,2);
console.log("\nSliced array is",slicedArray);

// Concatination of two arrays
let concatarray = array1.concat(array);
console.log("\nThe concated array is:",concatarray);

// map
console.log("\narray1 elements are:",array2);
const multipliedArray = array2.map(function (n) {
    return n * 2;
});
console.log("The array of map functions is:",multipliedArray);

// // filter
// const evenNumbers = multipliedArray.filter(function (element) {
//     return element % 2 === 0;
// });
// console.log("\nFiltering the even numbers:",evenNumbers);

// converting data type from int to string
let num = 8;
let convertedarray = num.toString();
console.log("\nThe converted array is:",convertedarray);
console.log("The converted array type is a:",typeof(convertedarray));