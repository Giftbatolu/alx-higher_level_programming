#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let b;
  for (b = 0; b < x; b++) {
    theFunction();
  }
};
