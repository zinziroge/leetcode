from itertools import product, combinations, combinations_with_replacement
import math
import random
import sys
import collections
from pathlib import Path
import bisect
import math
from typing import List

import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        y = 1
        for _ in range(abs(n)):
            y *= x

        if n >= 0:
            return y
        else:
            return 1/y
        """
        nbins = reversed(list(f"{abs(n):032b}"))
        z = 1
        x2 = x
        # x^1 = x^1
        # x^10 = x^8 * x^2
        for _, b in enumerate(nbins): # LSB -> ... -> MSB
            if b == '1':
                z *= x2
            x2 = x2 * x2  # x^2, x^4, x^8, ..., 
        
        if n >= 0:
            return z
        else:
            return 1/z


def q_50_top():
    if DEBUG_OUT:
        print(Solution().myPow(
            x = 2.00000, n = 10,
        ))
        print(Solution().myPow(
            x = 2.10000, n = 3,
        ))
        print(Solution().myPow(
            x = 2.00000, n = -2,
        ))
    

if __name__ == "__main__":
    q_50_top()
