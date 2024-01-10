#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node 100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    for (let i = 0; i < characterUrls.length; i++) {
      request(characterUrls[i], function (error, response, body) {
        if (error) {
          console.error('error:', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
