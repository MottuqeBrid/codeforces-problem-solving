"""
A. Stones on the Table
link: https://codeforces.com/problemset/problem/266/A
"""

import sys

n = int(sys.stdin.readline())
text = sys.stdin.readline().strip()

j = 0
for i in range(n):
    if i == (n - 1):
        break
    if text[i] == text[i + 1]:
        j += 1
print(j)
