#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node 2-statuscode.js <url>');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
