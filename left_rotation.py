#!/bin/python3

import math
import os
import random
import re
import sys

def rotLeft(nums, k):
    k = k % len(nums)
    count = start = len(nums)-1
    while count >=0 :
        cur = start
        prev = nums[start]
        while 1:
            nextt = (cur - k) % len(nums)
            nums[nextt], prev = prev, nums[nextt]
            cur  = nextt
            count -= 1
            if start == cur:
                break
        start -= 1
    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(*rotLeft(a,d))
