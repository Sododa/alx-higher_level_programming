#!/usr/bin/env node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch film data. Status code:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

