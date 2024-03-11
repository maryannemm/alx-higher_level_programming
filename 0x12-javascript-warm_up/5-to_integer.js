#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(firstArg);

// Check if the conversion was successful
if (!isNaN(num)) {
    console.log(`My number: ${num}`);
} else {
    console.log("Not a number");
}

