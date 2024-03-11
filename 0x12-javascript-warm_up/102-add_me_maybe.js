#!/usr/bin/node

// Define a function called "addMeMaybe" that increments the given number and calls the provided function
function addMeMaybe(number, theFunction) {
    number += 1;
    theFunction(number);
}

// Export the "addMeMaybe" function to make it visible from outside
module.exports = {
    addMeMaybe: addMeMaybe
};

