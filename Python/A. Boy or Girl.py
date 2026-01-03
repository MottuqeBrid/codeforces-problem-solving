"""
A. Boy or Girl
Codeforces: https://codeforces.com/problemset/problem/236/A
"""

import sys

input = sys.stdin.readline

name = input().strip().lower()
length_of_name = len(set(name))

if length_of_name % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
