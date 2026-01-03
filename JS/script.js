// 71A - Way Too Long Words --->	Node.js
const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const n = parseInt(input[0], 10);
const result = [];

for (let i = 1; i <= n; i++) {
  let word = input[i].trim();
  if (word.length > 10) {
    let firstChar = word[0];
    let lastChar = word[word.length - 1];
    let temp = firstChar + (word.length - 2) + lastChar;
    word = temp;
  }
  result.push(word);
}

console.log(result.join("\n"));


