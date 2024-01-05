#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, (error, response, body) => {
  if (error) throw error;
  const resp = JSON.parse(body);
  console.log(resp.title);
});
