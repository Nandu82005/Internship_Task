# Problem 5: String Validators
# HackerRank Link: https://www.hackerrank.com/challenges/string-validators/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
