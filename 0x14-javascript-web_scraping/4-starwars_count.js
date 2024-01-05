#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body).results;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
