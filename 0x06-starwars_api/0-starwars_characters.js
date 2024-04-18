#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];

export default async function nameloader(movie_id) {
    let res = [];

    const film = request(`https://swapi-api.alx-tools.com/api/films/${movie_id}`, (error, response, body) => {
        if (error) {
            return;
        }
        if (response.statusCode !== 200) {
          return;
        }
        
        return body;
    });
}


const result = nameloader(movie_id);
console.log(result);