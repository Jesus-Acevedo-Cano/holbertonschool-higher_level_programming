#!/usr/bin/node
// script that finds second biggest
function secondBig (a) {
  if (process.argv.length <= 3) {
    return 0;
  } else {
    a.sort((x, y) => x - y);
    a.pop();
    return (a.pop());
  }
}
console.log(secondBig(process.argv));
