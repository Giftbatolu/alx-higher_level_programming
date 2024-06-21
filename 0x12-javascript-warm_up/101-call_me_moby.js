#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let b;
  for (b = 0; b < 3; b++) {
    theFunction();
  }
};
