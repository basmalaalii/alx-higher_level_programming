#!/usr/bin/python3
count = 0
while count < 99:
    print("{:02d}, ".format(count), end=" ")
    count += 1
    if count == 99:
        print("{:02d} ".format(count), end=" ")
