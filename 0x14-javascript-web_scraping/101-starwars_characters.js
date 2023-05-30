#!/usr/bin/node
// A script that prints the title of a star wars movie

const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

try {
  request(url, function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      const allCharacters = JSON.parse(body).characters;
      for (let i = 0; i < allCharacters.length; i++) {
        request(allCharacters[i], function (err, res, body) {
          if (err) {
            console.log(err);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
} catch (e) {
  console.log(e);
}
