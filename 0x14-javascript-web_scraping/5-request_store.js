#!/usr/bin/node
// A script that displays the status code of a GET request

const fs = require('fs');
const request = require('request');

const url = process.argv[2];

const file = process.argv[3];

try {
  request(url, function (err, res, body) {
    if (err) {
      console.log('error:', err);
    } else {
      fs.writeFile(file, body, err => {
	if (err) {
          console.log(err);
	}
      });
    }
  });
} catch (e) {
  console.log(e);
}
