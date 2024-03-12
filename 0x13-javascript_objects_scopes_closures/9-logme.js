#!/usr/bin/node

/**
 * Prints the number of arguments already printed and the new argument value.
 *
 * @param {*} item - The argument value to print.
 */
exports.logMe = function (item) {
    if (!this.count) {
        this.count = 0; // Initialize the count if not already done
    }
    console.log(`${this.count}: ${item}`);
    this.count++;
};

