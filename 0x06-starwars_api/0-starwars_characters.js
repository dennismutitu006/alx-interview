#!/usr/bin/node
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const request = require('request');

function retrieve (urlChar) {
  return new Promise((resolve, reject) => {
    request(urlChar, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function printCharactersFromMovie (movieUrl) {
  try {
    const movieDat = await retrieve(movieUrl);
    const characters = JSON.parse(movieDat).characters;

    for (const characterUrl of characters) {
      const characterData = await retrieve(characterUrl);
      const characterName = JSON.parse(characterData).name;
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

request(url, (err, response, body) => {
  if (err) {
    throw err;
  } else {
    const movieDat = JSON.parse(body);
    printCharactersFromMovie(movieDaa.url);
  }
});
