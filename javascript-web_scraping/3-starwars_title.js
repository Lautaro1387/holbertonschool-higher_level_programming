#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, response, body) {
  if (error) {
    throw error;
  }
  console.log(JSON.parse(body).title);
});
