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
    def jump(self, nums: List[int]) -> int:
        n_nums = len(nums)
        n_jumps = [n_nums] * len(nums)
        n_jumps[0] = 0
        for i, n in enumerate(nums):
            for j in range(i+1, min(i+1+n, n_nums)):
                # index i から j へのjump
                # 2つ以上のたどり着き方があったらjump回数の少ない方を記憶する
                n_jumps[j] = min(n_jumps[i] + 1, n_jumps[j])

        return n_jumps[n_nums - 1]


def q_45_top():
    if DEBUG_OUT:
        print(Solution().jump(
             nums = [2,3,1,1,4]
        ))
        print(Solution().jump(
            nums = [2,3,0,1,4]
        ))

    
if __name__ == "__main__":
    q_45_top()
