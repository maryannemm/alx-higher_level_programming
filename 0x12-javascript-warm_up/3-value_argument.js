#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Print the appropriate message based on the argument
if (firstArg === undefined) {
    console.log("No argument");
} else {
    console.log(firstArg);
}

