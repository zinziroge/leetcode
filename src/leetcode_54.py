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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mat_ary = np.array(matrix)
        # w_step, h_step is size of each spiral.
        w_step = len(matrix[0])
        h_step = len(matrix) - 1
        n = mat_ary.shape[0] * mat_ary.shape[1]
        # (x,y) is start position
        x = 0
        y = 0
        # init
        #ans = [mat_ary[0, 0]]
        ans = []
        while True:
            # to right
            ans.extend(mat_ary[y, x:x+w_step].tolist())
            x += w_step - 1
            y += 1
            w_step = max(w_step - 1, 0)
            if len(ans)==n:
                break

            # to bottom
            ans.extend(mat_ary[y:y+h_step, x].tolist())
            y += h_step - 1
            x -= 1
            h_step = max(h_step - 1, 0)
            if len(ans)==n:
                break

            # to left
            ans.extend(reversed(mat_ary[y, x-w_step+1:x+1].tolist()))
            x -= w_step - 1
            y -= 1
            w_step = max(w_step - 1, 0)
            if len(ans)==n:
                break

            # to top
            ans.extend(reversed(mat_ary[y-h_step+1:y+1, x].tolist()))
            y -= h_step - 1
            x += 1
            h_step = max(h_step - 1, 0)
            if len(ans)==n:
                break

        return ans


def q_54_top():
    if DEBUG_OUT:
        print(Solution().spiralOrder(
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
        ))
        print(Solution().spiralOrder(
            matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        ))
        print(Solution().spiralOrder(
            [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        ))

    
if __name__ == "__main__":
    q_54_top()
