#!/usr/bin/node
// Write a script that writes a string to a file.

const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

try {
  fs.writeFile(filename, content, err => {
  if (err) {
    console.log(err);
	 }
  });
} catch(e) {
  console.log(e);
}
