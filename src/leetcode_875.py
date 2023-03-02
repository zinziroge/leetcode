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
        n = 0
        for pile in self.piles:
            n += pile // arg
            if n % arg != 0:
                n += 1
        return n <= self.h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        #ans = self.meguru_bisect(len(piles) - 1, sum(piles) + 1)
        ans = self.meguru_bisect(0, sum(piles) + 1)
        return ans


def q_875_top():
    if DEBUG_OUT:
        #print(Solution().minEatingSpeed(
        #    piles = [3,6,7,11], h = 8
        #))
        #print(Solution().minEatingSpeed(
        #    piles = [30,11,23,4,20], h = 5
        #))
        #print(Solution().minEatingSpeed(
        #    piles = [30,11,23,4,20], h = 6
        #))
        print(Solution().minEatingSpeed(
            piles=[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184],
            h=823855818,
        ))
    
if __name__ == "__main__":
    q_875_top()
