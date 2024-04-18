#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];

async function nameloader(movie_id) {
    return new Promise((resolve, reject) => {
        request(`https://swapi-api.alx-tools.com/api/films/${movie_id}`, (error, response, body) => {
            if (error) {
                reject(error);
            }
            if (response.statusCode !== 200) {
                reject(`Request failed with status code ${response.statusCode}`);
            }

            resolve(JSON.parse(body));
        });
    });
}

async function main() {
    try {
        const result = await nameloader(movie_id);
        console.log(result.characters);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
