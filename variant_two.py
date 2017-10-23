#!/usr/bin/env python3

# rewritten by me from C code
# C code author: @andreyorst

for i in range(0, 100):
    if not i % 3:
        print('Fizz', end='')
    if not i % 5:
        print('Buzz', end='')
    if i % 3 and i % 5:
        print(i, end='')
    print()
