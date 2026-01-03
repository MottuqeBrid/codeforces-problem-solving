// A. Team --> Node.js
const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const number = parseInt(input[0], 10);
let problem = 0;
for (let i = 1; i < input.length; i++) {
  const numbers = input[i].split("");
  let count = 0;
  for (let j = 0; j < numbers.length; j++) {
    if (numbers[j].trim() === "1") {
      count += 1;
    }
    if (count >= 2) {
      problem += 1;
      break;
    }
  }
}
console.log(problem);
