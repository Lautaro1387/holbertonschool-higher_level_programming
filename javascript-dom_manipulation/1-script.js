#!/usr/bin/node
/*
Write a JavaScript script that updates the text color
of the `header` element to red (`#FF0000`)
when the user clicks on the tag with id `red_header`
*/
const colors = document.querySelector('header').style.color = '#FF0000';
const clicked = document.addEventListener("click", colors);