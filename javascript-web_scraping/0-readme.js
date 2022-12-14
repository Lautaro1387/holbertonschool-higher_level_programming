#!/usr/bin/node
const argv = require('process').argv;

const fs = require('fs');
fs.readFile(argv[2], 'utf-8', function (error, response) {
    if (error) {
        return console.log(error);
    }
    console.log(response);
});