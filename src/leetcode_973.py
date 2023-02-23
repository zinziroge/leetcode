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
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [x**2 + y**2 for x, y in points]
        dist_index = [i[0] for i in sorted(enumerate(dist), key=lambda x:x[1])]
        ans = []
        for i in dist_index[:k]:
            ans.append(points[i])    
        return ans


def q_973_top():
    if DEBUG_OUT:
        print(Solution().kClosest(
            [[1,3],[-2,2]], 1,
        ))
        print(Solution().kClosest(
            [[3,3],[5,-1],[-2,4]],  2
        ))

    
if __name__ == "__main__":
    q_973_top()
