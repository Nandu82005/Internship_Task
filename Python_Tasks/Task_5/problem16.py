# Problem 16: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter


if __name__ == '__main__':
    X = int(input())
    shoe_sizes = Counter(map(int, input().split()))

    N = int(input())
    total = 0

    for _ in range(N):
        size, price = map(int, input().split())

        if shoe_sizes[size] > 0:
            total += price
            shoe_sizes[size] -= 1

    print(total)
