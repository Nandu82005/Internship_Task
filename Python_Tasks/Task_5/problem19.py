problem 19:# Merge the Tools
HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ""

        for char in substring:
            if char not in result:
                result += char

        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
