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
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0, n//2):
            m = n - i*2 - 1
            for j in range(0, m):
                #          [y][x] 
                y = i
                x = i + j
                lt = matrix[y][x]
                rt = matrix[x][n - 1 - y]
                rb = matrix[n - 1 - y][n - 1 - x]
                lb = matrix[n - 1 - x][y]

                matrix[y][x] = lb  # left top
                matrix[x][n - 1 - y] = lt  # right top
                matrix[n - 1 - y][n - 1 - x] = rt  # right bottom
                matrix[n - 1 - x][y] = rb  # left bottom



def q_48_top():
    if DEBUG_OUT:
        #matrix = [[1,2,3],[4,5,6],[7,8,9]]
        #Solution().rotate(matrix)
        #print(matrix)
        
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Solution().rotate(matrix)
        print(matrix)

    
if __name__ == "__main__":
    q_48_top()
