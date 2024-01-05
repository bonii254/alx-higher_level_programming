#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const completed = {};
    tasks.forEach((tasks) => {
      if (tasks.completed && completed[tasks.userId] === undefined) {
        completed[tasks.userId] = 1;
      } else if (tasks.completed) {
        completed[tasks.userId] += 1;
      }
    });
    console.log(completed);
  }
});
