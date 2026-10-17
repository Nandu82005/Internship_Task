problem 20:# Piling Up!
HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        cubes = deque(map(int, input().split()))

        top = float('inf')
        possible = True

        while cubes:
            if cubes[0] >= cubes[-1]:
                current = cubes.popleft()
            else:
                current = cubes.pop()

            if current > top:
                possible = False
                break

            top = current

        print("Yes" if possible else "No")
