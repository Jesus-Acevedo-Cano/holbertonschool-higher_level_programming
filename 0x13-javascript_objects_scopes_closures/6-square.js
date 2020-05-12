#!/usr/bin/node
// class square
class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let ht = 0; ht < this.height; ht++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
