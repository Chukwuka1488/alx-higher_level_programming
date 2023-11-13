#!/usr/bin/env node
// Script that prints "C is fun" x times, where x is the first argument

const args = process.argv.slice(2);
const numberOfTimes = parseInt(args[0]);

if (isNaN(numberOfTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfTimes; i++) {
    console.log('C is fun');
    }
}
