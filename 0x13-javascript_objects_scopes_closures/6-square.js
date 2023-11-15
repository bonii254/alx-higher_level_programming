#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const siz = this.height;
    for (let i = 0; i < siz; i++) {
      let row = '';
      for (let j = 0; j < siz; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
