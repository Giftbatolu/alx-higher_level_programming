#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const newnumber = number + 1;
  theFunction(newnumber);
};
