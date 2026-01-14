"""
A. Word
link: https://codeforces.com/problemset/problem/59/A
"""
import sys

text = sys.stdin.readline().strip()

numbers_of_uppercase = 0
for x in text:
    if x.isupper():
        numbers_of_uppercase += 1
if numbers_of_uppercase <= (len(text) - numbers_of_uppercase):
    print(text.lower())
else:
    print(text.upper())
