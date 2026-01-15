"""
A. Wrong Subtraction
link: https://codeforces.com/problemset/problem/977/A
"""

import sys

[n, k] = [int(x) for x in sys.stdin.readline().strip().split()]

for _ in range(k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1
print(n)
