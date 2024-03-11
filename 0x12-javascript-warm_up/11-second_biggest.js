#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Convert the arguments to integers
const integers = args.map(arg => parseInt(arg));

// Sort the integers in descending order
const sortedIntegers = integers.sort((a, b) => b - a);

// Check if there are at least two integers
if (sortedIntegers.length >= 2) {
    console.log(sortedIntegers[1]);
} else {
    console.log(0);
}

