#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: Missing movie ID argument');
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
    console.log(data.title);
  } else {
    console.error(`Error: Unable to fetch data. Status code: ${response.statusCode}`);
  }
});
