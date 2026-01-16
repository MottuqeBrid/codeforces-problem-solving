"""
Problem: A. Anton and Danik
Link: https://codeforces.com/problemset/problem/734/A
"""

n = int(input())
text = input().strip()

a = 0
d = 0
for i in range(n):
    if text[i] == "A":
        a += 1
    elif text[i] == "D":
        d += 1
if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")
