# Problem 9: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter


if __name__ == '__main__':
    n = int(input())
    words = []

    for i in range(n):
        words.append(input())

    counts = Counter(words)

    print(len(counts))
    print(*counts.values())
