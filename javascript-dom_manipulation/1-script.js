#!/usr/bin/node
/*
Write a JavaScript script that updates the text color
of the `header` element to red (`#FF0000`)
when the user clicks on the tag with id `red_header`
*/
const head = document.querySelector('header');
const clicked = document.querySelector('#red_header');
clicked.addEventListener("click", ()=>{
    head.style.color = '#FF0000';
  })