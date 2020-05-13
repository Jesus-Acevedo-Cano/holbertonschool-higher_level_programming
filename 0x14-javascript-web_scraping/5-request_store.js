#!/usr/bin/node
// write body response on a file
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, function(error) {
      if (error) {
        console.log(error);
      }
    })
  }
});
