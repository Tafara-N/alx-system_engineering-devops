#!/usr/bin/python3

for i in range(97, 123):
    if (i == 101) or (i == 113):
        continue
    print(chr(i).format(), end="")

