#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += c;
      }
      console.log(output);
    }
  }
}

module.exports = Square;
