#!/usr/bin/node
// A script that computes the number of tasks completed bu user id

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
let all_tasks = [];
const output = {};

try {
  request(url, function (err, res, body) {
    if (err) {
      console.log('error:', err);
    } else {
      all_tasks = JSON.parse(body);
      for (let i = 0; i < 10; i++) {
	let userId = i + 1;
	let count = 0;
	for (let j = 0; j < all_tasks.length; j++) {
	  if (all_tasks[j].userId == userId && all_tasks[j].completed) {
	    count++;
	  }
	}
	output[userId] = count;
      }
      console.log(output);
    }
  });
} catch (e) {
  console.log(e);
}
