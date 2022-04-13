#!/usr/bin/node
// script that prints the number of movies
// where the character "Wedge Antilles"

const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const result = JSON.parse(body).results;

    for (let i = 0; i < result.length; i++) {
      const characters = result[i].characters;
      for (let j = 0; j < characters.length; j++) {
        const check = characters[j].endsWith('18/');
        if (check) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
