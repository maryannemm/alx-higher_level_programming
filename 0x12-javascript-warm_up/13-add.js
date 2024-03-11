#!/usr/bin/node

// Define a function called "add" that takes two arguments and returns their sum
function add(a, b) {
    return a + b;
}

// Export the "add" function to make it visible from outside
module.exports = {
    add: add
};

