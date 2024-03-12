#!/usr/bin/node

// Import the dictionary from 101-data.js
const { dict } = require('./101-data');

// Initialize an empty object to store the new dictionary
const occurrencesById = {};

// Iterate through the original dictionary
for (const userId in dict) {
    const occurrences = dict[userId];
    if (!occurrencesById[occurrences]) {
        // If the occurrences key doesn't exist in the new dictionary, create it
        occurrencesById[occurrences] = [userId];
    } else {
        // Otherwise, append the user ID to the existing list
        occurrencesById[occurrences].push(userId);
    }
}

// Print the new dictionary
console.log(occurrencesById);

