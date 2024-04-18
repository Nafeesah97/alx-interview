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

async function characters(characters_url) {
    return new Promise((resolve, reject) => {
        request(`${characters_url}`, (error, response, body) => {
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
    let final_chars = [];
    try {
        const result = await nameloader(movie_id);
        const characters_urls = result.characters;
        for (let chars in characters_urls) {
            const char_result = await characters(chars);
            final_chars.push(char_result.name)
        };
    console.log(final_chars);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
