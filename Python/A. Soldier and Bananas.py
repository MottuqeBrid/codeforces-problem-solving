"""
A. Soldier and Bananas
link: https://codeforces.com/problemset/problem/546/A
"""

# k 2k 3k
# W banana
# n dollars

import sys

[k, n, w] = list(int(x) for x in sys.stdin.readline().strip().split())

total_cost = 0

for i in range(w):
    total_cost = k * (i + 1) + total_cost

if total_cost <= n:
    print(0)
else:
    print(total_cost - n)
