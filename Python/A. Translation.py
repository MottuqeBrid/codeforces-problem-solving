"""
Problem: A. Translation
Link: https://codeforces.com/problemset/problem/41/A
"""
s = input().strip()
t = input().strip()

s_rev = s[::-1]
if s_rev == t:
    print("YES")
else:
    print("NO")
