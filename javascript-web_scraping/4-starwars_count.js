#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: Missing API URL argument');
  process.exit(1);
}

const wedgeAntillesId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach((film) => {
      if (film.characters.some((url) => url.includes(`/people/${wedgeAntillesId}/`))) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.error(`Error: Unable to fetch data. Status code: ${response.statusCode}`);
  }
});
