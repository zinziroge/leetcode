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
    def maxSubArray(self, nums: List[int]) -> int:
        sp = 0
        ep = 1
        max_s = nums[0]
        prev_s = nums[0]
        while True:
            if ep == len(nums):
                break

            if sum(nums[sp:ep+1]) > prev_s or ep-sp==1:
                ep += 1
            else:
                sp += 1


            s = sum(nums[sp:ep])

            if s > max_s:
                max_s = s

            prev_s = s


        return max_s


def q_53_top():
    if DEBUG_OUT:
        #print(Solution().maxSubArray(
        #    nums = [-2,1,-3,4,-1,2,1,-5,4]
        #))
        #print(Solution().maxSubArray(
        #    nums = [1]
        #))
        print(Solution().maxSubArray(
            nums = [5,4,-1,7,8]
        ))
    

if __name__ == "__main__":
    q_53_top()
