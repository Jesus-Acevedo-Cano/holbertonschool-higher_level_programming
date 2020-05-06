#!/usr/bin/node
// export func
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
