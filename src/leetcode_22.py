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
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for i in range(2**(n*2)):
            o_cnt = 0
            c_cnt = 0
            s = ""
            is_valid = True
            print(i)
            for b in list(f"{i:0{2*n}b}"):
                if b=="0":
                    o_cnt += 1
                    s += "("
                else:
                    c_cnt += 1
                    s += ")"

                if o_cnt < c_cnt or n < o_cnt or n < c_cnt:
                    is_valid = False
                    break

            if is_valid:
                ans.append(s)

        return ans

def q_22_top():
    if DEBUG_OUT:
        print(Solution().generateParenthesis(
            3
        ))
        print(Solution().generateParenthesis(
            1
        ))

    
if __name__ == "__main__":
    q_22_top()
