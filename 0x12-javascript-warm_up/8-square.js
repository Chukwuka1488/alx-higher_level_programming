#!/usr/bin/env node
// Script that prints a square of a given size without using repeat

const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (isNaN(size) || size < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
    console.log(line);
  }
}
