#!/usr/bin/node

// Define a function called "factorial" that computes the factorial recursively
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Get the first argument passed to the script
const numArg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(numArg);

// Check if the conversion was successful
if (!isNaN(num)) {
    // Compute the factorial and print the result
    const result = factorial(num);
    console.log(result);
} else {
    console.log("Factorial of NaN is 1");
}

