"""
Problem: A. Beautiful Year
Link: https://codeforces.com/problemset/problem/271/A
"""
y = input().strip()

y_int = int(y)

i = 1
while True:
    a = set([x for x in str(y_int + i)])
    if len(a) == 4:
        print(y_int + i)
        break
    else:
        i += 1
