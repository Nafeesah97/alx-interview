#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

async function nameloader (movieId) {
  return new Promise((resolve, reject) => {
    request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      }

      resolve(JSON.parse(body));
    });
  });
}

async function characters (charactersUrl) {
  return new Promise((resolve, reject) => {
    request(`${charactersUrl}`, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      }

      resolve(JSON.parse(body));
    });
  });
}

async function main () {
  const finalChars = [];
  try {
    const result = await nameloader(movieId);
    const charactersUrls = result.characters;
    for (const chars of charactersUrls) {
      const charResult = await characters(chars);
      finalChars.push(charResult.name);
    }
    for (const name of finalChars) {
      console.log(name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
