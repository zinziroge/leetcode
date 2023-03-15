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


import itertools


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_s = ""
        for i, c in enumerate(s):
            # left_s(includeing c), right_s
            # 0,                 i, i+1
            n = min(i, len(s) - i)
            left_s = s[:i]
            right_s = s[i:]
            left_s = left_s[::-1][:n]
            right_s = right_s[:n]

            sub_s = ""
            for l, r in zip(list(left_s), list(right_s)):
                if l==r:
                    sub_s = l + sub_s + r
                else:
                    break
            if len(longest_s) < len(sub_s):
                longest_s = sub_s

        for i, c in enumerate(s):
            # left_s, c, right_s
            # 0, i-1, i, i+1
            n = min(i, len(s) - i)
            left_s = s[:i]
            right_s = s[i+1:] 
            left_s = left_s[::-1][:n]
            right_s = right_s[:n]

            sub_s = c
            for l, r in zip(list(left_s), list(right_s)):
                if l==r:
                    sub_s = l + sub_s + r
                else:
                    break
            if len(longest_s) < len(sub_s):
                longest_s = sub_s

        return longest_s


def q_5_top():
    if DEBUG_OUT:
        print(Solution().longestPalindrome(
            "eabcb"
        ))
        print(Solution().longestPalindrome(
            s = "abb"
        ))
        print(Solution().longestPalindrome(
            s = "babad"
        ))
        print(Solution().longestPalindrome(
            s = "cbbd"
        ))

    
if __name__ == "__main__":
    q_5_top()
