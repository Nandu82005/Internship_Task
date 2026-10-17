# Problem 7: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))

    N = int(input())
    b = set(map(int, input().split()))

    result = a.symmetric_difference(b)

    for num in sorted(result):
        print(num)
