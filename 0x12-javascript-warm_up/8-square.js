#!/usr/bin/node

const { argv } = require('process');

let b, d;
let pattern;

const size = parseInt(argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
}
for (b = 0; b < size; b++) {
  pattern = '';
  for (d = 0; d < size; d++) {
    pattern += 'X';
  }
  console.log(pattern);
}
