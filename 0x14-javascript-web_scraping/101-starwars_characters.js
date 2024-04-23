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
      console.error(`Error fetching film data: ${error}`);
    } else {
      const data = JSON.parse(body);
      const charactersUrls = data.characters;
      const promises = [];

      charactersUrls.forEach((characterUrl) => {
        promises.push(new Promise((resolve, reject) => {
          request({
            url: characterUrl,
            rejectUnauthorized: false // Ignore SSL certificate verification
          }, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        }));
      });

      Promise.all(promises)
        .then((characters) => {
          characters.forEach((character) => {
            console.log(character);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    }
  });
}

fetchMovieCharacters(apiUrl);

