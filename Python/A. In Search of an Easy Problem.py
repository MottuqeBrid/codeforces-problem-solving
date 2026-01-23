"""
Problem: A. In Search of an Easy Problem
Link: https://codeforces.com/problemset/problem/1030/A
"""


n = int(input())

problems = [int(x) for x in input().strip().split()]

j = 0
for i in problems:
    if i == 0:
        continue
    else:
        j += 1
        break


if j == 0:
    print("EASY")
else:
    print("HARD")
