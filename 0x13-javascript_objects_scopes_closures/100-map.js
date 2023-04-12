#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((num, i) => num * i);
console.log(list);
console.log(newList);
