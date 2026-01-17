"""
Problem: A. Vanya and Fence
Link: https://codeforces.com/problemset/problem/677/A
"""

[n, h] = [int(x) for x in input().strip().split()]

friends_height = [int(x) for x in input().strip().split()]

w = 0
for i in range(n):
    if friends_height[i] <= h:
        w += 1
    else:
        w += 2

print(w)
