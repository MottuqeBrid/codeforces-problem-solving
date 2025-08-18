// A. Watermelon

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();

const n = parseInt(input, 10);

if (n % 2 === 0 && n >= 4) {
  console.log("YES");
} else {
  console.log("NO");
}
