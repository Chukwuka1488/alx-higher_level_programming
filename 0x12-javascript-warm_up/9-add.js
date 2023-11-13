#!/usr/bin/node
// Script that prints the addition of two integers

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
const firstNum = parseInt(args[0]);
const secondNum = parseInt(args[1]);

const result = add(firstNum, secondNum);
console.log(result);
