#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

// Define a function called "incr" that increments the value property
myObject.incr = function() {
    this.value += 1;
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

