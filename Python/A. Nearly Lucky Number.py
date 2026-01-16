"""
A. Nearly Lucky Number
link: https://codeforces.com/problemset/problem/110/A
"""

import sys

number = sys.stdin.readline().strip()

n = 0

for i in number:
    if i == "4" or i == "7":
        n += 1
if n == 4 or n == 7:
    print("YES")
else:
    print("NO")
