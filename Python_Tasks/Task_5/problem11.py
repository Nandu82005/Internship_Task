problem 11:# Text Wrap
HackerRank Link: https://www.hackerrank.com/challenges/text-wrap/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
