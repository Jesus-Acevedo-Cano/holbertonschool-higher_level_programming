#!/usr/bin/node
// completed tasks nbr for each user
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const compTasks = {};
    JSON.parse(body).forEach(element => {
      if (element.completed) {
        if (compTasks[element.userId]) {
          compTasks[element.userId] = compTasks[element.userId] + 1;
        } else {
          compTasks[element.userId] = 1;
        }
      }
    });
    console.log(compTasks);
  }
});
