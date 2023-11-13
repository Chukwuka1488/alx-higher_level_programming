#!/usr/bin/node
// File: 102-add_me_maybe.js

function addMeMaybe(number, theFunction) {
  theFunction(number + 1);
}

module.exports.addMeMaybe = addMeMaybe;
