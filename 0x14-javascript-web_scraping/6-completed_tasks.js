#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(task => {
      if (task.completed) {
        const userId = task.userId;
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    });

    console.log(completedTasksByUser);
  }
});

