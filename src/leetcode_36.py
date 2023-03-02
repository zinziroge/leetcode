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


import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ary = np.empty((9, 9), dtype=int)

        for i_row, row in enumerate(board):
            for i_col, v in enumerate(row):
                if v==".":
                    v = 0
                else:
                    v = int(v)
                ary[i_row, i_col] = v

        print(ary)

        # row
        for i in range(9):
            vv = ary[i,:].tolist()
            cnt = [0] * 10
            for v in vv:
                if v!=0 and cnt[v]==1:
                    return False
                else:
                    cnt[v]=1
                
        # col
        for i in range(9):
            vv = ary[:,i].tolist()
            cnt = [0] * 10
            for v in vv:
                if v!=0 and cnt[v]==1:
                    return False
                else:
                    cnt[v]=1

        # 3x3 block
        for x in range(0,9,3):
            for y in range(0,9,3):
                cnt = [0] * 10
                vv = ary[y:y+3,x:x+3].reshape(9,).tolist()
                for v in vv:
                    if v!=0 and cnt[v]==1:
                        return False
                    else:
                        cnt[v]=1

        return True


def q_36_top():
    if DEBUG_OUT:
        print(Solution().isValidSudoku(
            [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
        ))
        print(Solution().isValidSudoku(
            [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
        ))

    
if __name__ == "__main__":
    q_36_top()
