
import math
import os
import random
import re
import sys


def repeatedString(s, n):
    l = len(s)
    count = 0
    for i in s:
        if i == "a":
            count += 1
    if count == 0:
        return 0
    res = count * (n//l)
    for i in range(n%l):
        if s[i] == "a":
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
