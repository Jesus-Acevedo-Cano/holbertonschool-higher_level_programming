#!/usr/bin/node
// script that prints a xquare
let i;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('x'.repeat(process.argv[2]));
  }
}
