#!/usr/bin/node
// A script that computes the number of tasks completed bu user id

const request = require('request');

const url = process.argv[2];
let allTasks = [];
const output = {};

try {
  request(url, function (err, res, body) {
    if (err) {
      console.log('error:', err);
    } else {
      allTasks = JSON.parse(body);
      for (let i = 0; i < 10; i++) {
        const userId = i + 1;
        let count = 0;
        for (let j = 0; j < allTasks.length; j++) {
          if (allTasks[j].userId === userId && allTasks[j].completed) {
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
