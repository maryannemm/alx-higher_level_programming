#!/usr/bin/node

/**
 * Returns the reversed version of the given list.
 *
 * @param {Array} list - The list to reverse.
 * @returns {Array} - The reversed list.
 */
exports.esrever = function (list) {
    const reversedList = [];
    for (let i = list.length - 1; i >= 0; i--) {
        reversedList.push(list[i]);
    }
    return reversedList;
};

