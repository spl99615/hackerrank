
import math
import os
import random
import re
import sys
from collections import defaultdict


def maxDifference(a):
    diffdict = defaultdict(list)
    maxdiff = []

    for i, val in enumerate(reversed(a)):
        diffarr = []
        for val1 in a[:len(a) - i]:
            if val > val1:
                diffarr.append(val - val1)
        if diffarr:
            diffdict[str(i) + str(val)] = diffarr
        else:
            diffdict[str(i) + str(val)] = [-1]
    for vals in diffdict.values():
        maxdiff += vals
    return max(maxdiff)


if __name__ == '__main__':
    print(maxDifference([1, 2, 6, 4, 5, 1, 2, 10]))
