#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        /**
         * Initializes a Rectangle instance with given width and height.
         *
         * @param {number} w - Width of the rectangle.
         * @param {number} h - Height of the rectangle.
         */
        if (w <= 0 || h <= 0) {
            // Create an empty object if width or height is not positive
            return {};
        }
        this.width = w;
        this.height = h;
    }

    print() {
        /**
         * Prints the rectangle using the character 'X'.
         */
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }

    rotate() {
        /**
         * Exchanges the width and the height of the rectangle.
         */
        [this.width, this.height] = [this.height, this.width];
    }

    double() {
        /**
         * Multiplies the width and the height of the rectangle by 2.
         */
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;

