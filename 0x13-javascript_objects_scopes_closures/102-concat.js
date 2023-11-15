#!/usr/bin/node
// This script concats 2 files

const fs = require('fs');

let fileA = fs.readFileSync(process.argv[2], 'utf8');
let fileB = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], fileA + fileB);