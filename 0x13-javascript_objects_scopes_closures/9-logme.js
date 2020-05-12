#!/usr/bin/node
// print arg nbr and item
let nb = 0;
exports.logMe = function (item) {
  console.log('%d: %s', nb, item);
  nb++;
};
