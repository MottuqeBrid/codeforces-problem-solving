const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
const [m1, n1] = input.split(" ");

const m = parseInt(m1, 10);
const n = parseInt(n1, 10);
if (1 <= m && m <= n && n <= 16) {
  const dominoes = (m * n) / 2;
  console.log(Math.floor(dominoes));
}
