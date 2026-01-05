"""
A. Elephant
Codeforces: https://codeforces.com/problemset/problem/617/A
"""
x = int(input())

steps = x // 5
if x % 5 != 0:
    steps += 1
print(steps)
