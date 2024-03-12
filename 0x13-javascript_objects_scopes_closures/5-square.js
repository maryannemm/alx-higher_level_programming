#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
        /**
         * Initializes a Square instance with given size.
         *
         * @param {number} size - Size of the square (both width and height).
         */
        super(size, size); // Call the constructor of the parent class (Rectangle)
    }
}

module.exports = Square;

