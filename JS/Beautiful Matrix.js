const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");
let num = 0;
for (let i = 0; i < 5; i++) {
  if (input[i].includes("1")) {
    const rowNumbers = input[i].split(" ");
    for (let j = 0; j < 5; j++) {
      if (rowNumbers[j].includes("1")) {
        num = Math.abs(i - 2) + Math.abs(j - 2);
      }
    }
  }
}
console.log(num);
