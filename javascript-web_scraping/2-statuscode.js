#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request(argv[2], function (error, response, statusCode) {
  if (error) {
    throw error;
  }
  console.log('code:', response && response.statusCode);
});
