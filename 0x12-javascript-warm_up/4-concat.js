#!/usr/bin/node

const { argv } = require('process');

const firstarg = argv[2];
const secondarg = argv[3];
console.log(`${firstarg} is ${secondarg}`);
