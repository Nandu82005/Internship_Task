# Problem 6: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def average(array):
    arr = set(array)
    return round(sum(arr) / len(arr), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
