"""
Problem: A. Tram
Link: https://codeforces.com/problemset/problem/116/A
"""

n = int(input().strip())

k = 0
j = 0
for i in range(n):
    [a, b] = [int(x) for x in input().strip().split()]
    k = k - a + b
    if k > j:
        j = k
print(j)
