#!/usr/bin/node

// Get the first argument passed to the script
const sizeArg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(sizeArg);

// Check if the conversion was successful
if (!isNaN(size) && size > 0) {
    // Print the square using the character 'X'
    for (let i = 0; i < size; i++) {
        console.log("X".repeat(size));
    }
} else {
    console.log("Missing size");
}

