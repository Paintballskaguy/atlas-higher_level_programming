#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: Missing API URL argument');
  process.exit(1);
}

// Make the GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    console.log(completedTasks);
  } else {
    console.error(`Error: Unable to fetch data. Status code: ${response.statusCode}`);
  }
});
