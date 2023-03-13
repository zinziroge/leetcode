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


import numpy as np
import itertools


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i, n in enumerate(nums):
            if dp[i]:
                for nn in range(1, n+1):
                    dp[min(len(nums) - 1, i+nn)] = True
            #for j, t in enumerate(reversed(nums[:i])):
            #    #print(j,t)
            #    j = len(nums[:i]) - 1 - j
            #    if dp[j] and i <= j+t:
            #        dp[i] = True
            #        break
            #
            #for j, t in enumerate(nums[:i]):
            #    if dp[j] and i <= j+t:
            #        dp[i] = True
            #        break

        return dp[len(nums) - 1]


def q_55_top():
    if DEBUG_OUT:
        print(Solution().canJump(
             nums = [2,3,1,1,4]
        ))
        print(Solution().canJump(
            nums = [3,2,1,0,4]
        ))
        print(Solution().canJump(
            nums = [0,2,3],
        ))

    
if __name__ == "__main__":
    q_55_top()
