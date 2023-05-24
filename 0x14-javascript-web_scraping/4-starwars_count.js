#!/usr/bin/node
// A script that prints the title of a star wars movie

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const allMovies = JSON.parse(body).results;
    const filteredMovies = allMovies.filter((movie) =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(filteredMovies.length);
  }
});
