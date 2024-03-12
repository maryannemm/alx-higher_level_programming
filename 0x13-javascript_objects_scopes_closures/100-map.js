#!/usr/bin/node

// Import the list from 100-data.js
const { list } = require('./100-data');

// Compute a new list where each value is equal to the value of the initial list multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);

