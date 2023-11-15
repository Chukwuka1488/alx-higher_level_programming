#!/usr/bin/node
// File: 2-rectangle.js
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
    }
  }
}

module.exports = Rectangle;
