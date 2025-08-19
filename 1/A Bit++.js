const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const number = parseInt(input[0], 10);

let initialValue = 0;

for (let i = 1; i <= number; i++) {
  const numVar = input[i].trim();
  if (numVar.includes("++")) {
    initialValue += 1;
  } else if (numVar.includes("--")) {
    initialValue -= 1;
  }
}
console.log(initialValue);
