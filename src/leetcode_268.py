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
    def missingNumber(self, nums: List[int]) -> int:
        self.nums = sorted(nums)
        a = self.meguru_bisect(-1, len(self.nums))
        return(a)

    def meguru_bisect(self, ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if self.is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(self, arg):
        #print(arg)
        # 条件を満たすかどうか？問題ごとに定義
        return self.nums[arg] != arg


def q_268_top():
    if DEBUG_OUT:
        print(Solution().missingNumber(
            [3,0,1],
        ))
        print(Solution().missingNumber(
            [0,1],
        ))
        print(Solution().missingNumber(
            [9,6,4,2,3,5,7,0,1],
        ))

    
if __name__ == "__main__":
    q_268_top()
