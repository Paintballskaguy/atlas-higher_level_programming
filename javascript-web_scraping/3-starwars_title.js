#!/usr/bin/node

const request = require('request');
const movieId = process.argvp[2];

if (!movieId) {
  console.error('Error: Missing movie ID arguement');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.data(data.title);
  } else {
    console.error(`Error: Unable to fetch data. Status code: ${response.statusCode}`);
  }
});
