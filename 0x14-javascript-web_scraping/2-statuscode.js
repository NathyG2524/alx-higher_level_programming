#!/usr/bin/node
// script that display the status code of a GET request

const fs = require('request');
const url = process.argv[2];

fs(url, function (error, response, body) {
  if (err) {
    console.error(err);
  } else console.log('code:', response.statusCode);
});
