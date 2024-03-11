#!/usr/bin/node

// Define a function called "add" that takes two arguments and returns their sum
function add(a, b) {
    return a + b;
}

// Get the first and second arguments passed to the script
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if both arguments are valid integers
if (!isNaN(num1) && !isNaN(num2)) {
    // Call the "add" function and print the result
    console.log(add(num1, num2));
} else {
    console.log("NaN");
}

