"""
A. Petya and Strings
Codeforces: https://codeforces.com/problemset/problem/112/A
"""

import sys

input = sys.stdin.readline

s1 = input().strip().lower()
s2 = input().strip().lower()

k = 0
for i in range(len(s1)):
    if s1[i] < s2[i]:
        k = -1
        break
    elif s1[i] > s2[i]:
        k = 1
        break
    else:
        continue
print(k)
