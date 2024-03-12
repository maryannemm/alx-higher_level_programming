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

    charPrint(c = 'X') {
        /**
         * Prints the square using the character c.
         *
         * @param {string} c - Character to print (default is 'X').
         */
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = Square;

