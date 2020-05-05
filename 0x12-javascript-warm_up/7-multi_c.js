#!/usr/bin/node
// script that prints x times “C is fun”
let i;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
