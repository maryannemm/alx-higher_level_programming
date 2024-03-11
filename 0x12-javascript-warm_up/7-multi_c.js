#!/usr/bin/node

// Get the first argument passed to the script
const numArg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(numArg);

// Check if the conversion was successful
if (!isNaN(num)) {
    // Print "C is fun" x times
    for (let i = 0; i < num; i++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}

