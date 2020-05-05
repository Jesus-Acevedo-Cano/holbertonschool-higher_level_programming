#!/usr/bin/node
// script that prints My number
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: %i', process.argv[2]);
}
