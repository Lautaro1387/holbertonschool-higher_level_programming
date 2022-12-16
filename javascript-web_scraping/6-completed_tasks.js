#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

request(argv[2], function (error, response, body) {
  if (error) {
    throw error;
  }
  const task = {};
  const all = JSON.parse(body);
  for (let i = 0; i < all.length; i++) {
    if (all[i].completed === true) {
      if (all[i].userId in task) {
        task[all[i].userId] += 1;
      } else {
        task[all[i].userId] = 1;
      }
    }
  }
  console.log(task);
});
