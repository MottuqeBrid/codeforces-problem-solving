"""
A. Bear and Big Brother
link: https://codeforces.com/problemset/problem/791/A
"""

input_numbers = input().strip().split()

[limak, bob] = [int(x) for x in input_numbers]

i = 0
while True:
    if limak <= bob:
        i = i + 1
        limak = limak * 3
        bob = bob * 2
    else:
        print(i)
        break