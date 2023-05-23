#!/usr/bin/node
//Write a script that reads and prints the content of a file.

const fs = require('fs')
let filename = process.argv[2];

try {
	let content = fs.readFileSync(filename, 'utf8');
	console.log(content)
} catch(e) {
	console.log(e)
}
