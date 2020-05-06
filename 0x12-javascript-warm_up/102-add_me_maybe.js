#!/usr/bin/node
// export func
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number += 1);
};
