#!/usr/bin/node
const dict = require("./101-data").dict;
let obj = {};
const keys = Object.values(dict);
const arr = Object.entries(dict);
for (let key of keys) {
	obj[key] = [];
}
for (let i = 0; i < arr.length;) {
	if (arr[i][1] in obj) obj[arr[i][1]].push(arr[i][0])
	i++;
}

console.log(obj);
