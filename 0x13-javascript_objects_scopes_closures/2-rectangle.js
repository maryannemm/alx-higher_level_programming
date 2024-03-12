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
}

module.exports = Rectangle;

