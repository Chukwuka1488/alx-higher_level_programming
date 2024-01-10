#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: node 6-completed_tasks.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        const userId = tasks[i].userId;
        if (completedTasks[userId]) {
          completedTasks[userId]++;
        } else {
          completedTasks[userId] = 1;
        }
      }
    }

    console.log(completedTasks);
  }
});
