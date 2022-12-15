#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request(argv[2], function (error, response, body) {
  if (error) {
    throw error;
  }
  let count = 0;
  const all = JSON.parse(body).results;
  for (let i = 0; i < all.length; i++) {
    for (let j = 0; j < all[i].characters.length; j++) {
      if (all[i].characters[j].includes('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
