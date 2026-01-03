// A. Next Round
const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");
const [n1, k1] = input[0].split(" ");
const n = parseInt(n1, 10);
const k = parseInt(k1, 10);
let count = 0;
if (1 <= k && k <= n && n <= 50) {
  const particepent = input[1].split(" ");
  const kThScore = parseInt(particepent[k - 1], 10);
  for (let i = 0; i < n; i++) {
    const score = parseInt(particepent[i], 10);
    if (score > 0 && score >= kThScore) {
      count++;
    }
  }
  console.log(count);
} else {
  console.log(0);
}
