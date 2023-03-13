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
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        nums_sorted = sorted(nums)

        max_seq = 1
        n_seq = 1
        prev_v = nums_sorted.pop(0)
        for v in nums_sorted:
            if prev_v + 1==v:
                n_seq += 1
                if n_seq > max_seq:
                    max_seq = n_seq
            elif prev_v==v:
                ...
            else:
                # reset
                n_seq = 1

            prev_v = v

        return max_seq


def q_128_top():
    if DEBUG_OUT:
        print(Solution().longestConsecutive(
            nums = [100,4,200,1,3,2]
        ))
        print(Solution().longestConsecutive(
            nums = [0,3,7,2,5,8,4,6,0,1]
        ))
        print(Solution().longestConsecutive(
            nums = []
        ))
        print(Solution().longestConsecutive(
            [1,2,0,1]
        ))

    
if __name__ == "__main__":
    q_128_top()
