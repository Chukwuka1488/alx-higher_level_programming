#!/usr/bin/node
// Script that finds the second biggest integer in the list of arguments

function findSecondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  const numbers = args.map(Number); // Convert all arguments to numbers
  const uniqueNumbers = Array.from(new Set(numbers)); // Remove duplicates
  uniqueNumbers.sort((a, b) => b - a); // Sort in descending order

  return uniqueNumbers[1]; // Return the second element
}

const args = process.argv.slice(2);

console.log(findSecondBiggest(args));
