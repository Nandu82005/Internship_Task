# Problem 17: No Idea!
# HackerRank Link: https://www.hackerrank.com/challenges/no-idea/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    happiness = 0

    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1

    print(happiness)
