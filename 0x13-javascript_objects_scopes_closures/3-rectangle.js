#!/usr/bin/node
// class Rectangle and print with X
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ht = 0; ht < this.height; ht++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
