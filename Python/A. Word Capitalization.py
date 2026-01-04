"""
A. Word Capitalization
Codeforces: https://codeforces.com/problemset/problem/281/A
"""

word = input().strip()
new_word = word[0].upper() + word[1:]
print(new_word)