#!/usr/bin/node

/**
 * Returns a function that converts a number from base 10 to the specified base.
 *
 * @param {number} base - The target base (e.g., 2, 8, 16, etc.).
 * @return {function} - A function that converts a number from base 10 to the specified base.
 */
exports.converter = function (base) {
    /**
     * Converts a number from base 10 to the specified base.
     *
     * @param {number} number - The number to convert.
     * @return {string} - The converted number in the specified base.
     */
    function convertToBase(number) {
        if (base === 16) {
            return number.toString(16);
        } else if (base === 10) {
            return number.toString();
        } else {
            return number.toString(base);
        }
    }

    return convertToBase;
};

