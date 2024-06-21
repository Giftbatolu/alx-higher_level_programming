#!/usr/bin/node

const { argv } = require('process');
let b;

const num = parseInt(argv[2], 10);
if (!isNaN(num)) {
  for (b = 0; b < num; b++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
