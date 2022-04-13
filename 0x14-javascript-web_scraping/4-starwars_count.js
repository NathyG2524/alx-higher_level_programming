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
      for (let j = 0; j < result[i].characters; j++) {
        if (result[i].characters.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
