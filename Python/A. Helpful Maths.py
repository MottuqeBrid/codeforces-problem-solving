"""
A. Helpful Maths
Link: https://codeforces.com/problemset/problem/339/A
"""

input = input()
numbers = [int(i) for i in input.split("+")]

numbers.sort()
print("+".join([str(i) for i in numbers]))
