#!/usr/bin/python3
for i in range(ord('a'), ord('z')-1, -1):
    print(chr(i) if i % 2 == 0 else chr(i).upper(), end='')
