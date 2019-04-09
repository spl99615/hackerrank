#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'getMaxOccurrences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER minLength
#  3. INTEGER maxLength
#  4. INTEGER maxUnique
#

def getMaxOccurences(s, minLength, maxLength, maxUnique):
    length = len(s)
    substring_chars = defaultdict(int)
    substrings = []
    count = 0
    for _ in (x for x in s):
        for j in range(count + minLength, count + maxLength + 1):
            if j > length:
                continue
            substring = s[count:j]
            print("i:{},j:{},substring:::{}".format(count, j, substring))
            # if len(substring) >= minLength and len(substring) <= maxLength and len(set(substring)) <= maxUnique:
            if len(set(substring)) <= maxUnique:
                substrings.append(substring)
                substring_chars[substring] += 1
        count += 1
    print(substrings)
    print(substring_chars)
    return max(substring_chars.values())


if __name__ == '__main__':
    print(getMaxOccurences('abcde', 2, 4, 26))
    print(getMaxOccurences('ababab', 2, 3, 4))
