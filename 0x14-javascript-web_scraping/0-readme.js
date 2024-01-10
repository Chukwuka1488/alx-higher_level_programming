#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
  console.log('Usage: node 0-readme.js <filepath>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
