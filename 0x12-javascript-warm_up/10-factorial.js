#!/usr/bin/node
// script that computes and prints a factorial
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (parseInt(a) === 0) {
    return 1;
  } else {
    return parseInt(a) * factorial(parseInt(a) - 1);
  }
}
console.log(factorial(process.argv[2]));
