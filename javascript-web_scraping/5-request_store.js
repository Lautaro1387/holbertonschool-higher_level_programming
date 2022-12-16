#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    throw error;
  }
  fs.writeFile(argv[3], body, 'utf-8', function (error) {
    if (error) {
      throw error;
    }
  });
});
