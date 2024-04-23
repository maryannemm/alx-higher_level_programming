#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

function fetchMovieCharacters(url) {
  request({
    url,
    rejectUnauthorized: false // Ignore SSL certificate verification
  }, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      console.log(`Characters in ${data.title}:`);
      data.characters.forEach((characterUrl) => {
        request({
          url: characterUrl,
          rejectUnauthorized: false // Ignore SSL certificate verification
        }, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

fetchMovieCharacters(apiUrl);

