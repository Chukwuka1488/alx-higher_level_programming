#!/usr/bin/node
// first argument can be converted to an integer

const firstArg = process.argv[2];
const number = parseInt(firstArg);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
