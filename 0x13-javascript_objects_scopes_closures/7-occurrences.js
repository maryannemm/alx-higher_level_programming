#!/usr/bin/node

/**
 * Returns the number of occurrences of `searchElement` in the given list `lst`.
 *
 * @param {Array} lst - The list to search in.
 * @param {*} searchElement - The element to search for.
 * @returns {number} - The number of occurrences of `searchElement` in `lst`.
 */
exports.nbOccurences = function (lst, searchElement) {
    return lst.filter(element => element === searchElement).length;
};

