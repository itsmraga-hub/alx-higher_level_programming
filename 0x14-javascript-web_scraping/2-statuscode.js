#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

try {
  request(url, function (err, res, body) {
    if (err) {
      console.log('error:', err);
    } else {
      console.log('code:', res.statusCode);
    }
  });
} catch (e) {
  console.log(e);
}
