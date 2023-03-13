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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for v in range(2**n):
            bins_str = f"{v:{n}b}"
            a = []
            for j, c in enumerate(list(bins_str)):
                if c=="1":
                    a.append(nums[j])
            ans.append(a)

        return ans



def q_78_top():
    if DEBUG_OUT:
        print(Solution().subsets(
            [1,2,3]))
        print(Solution().subsets(
            [0]))

    
if __name__ == "__main__":
    q_78_top()
