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
        # 条件を満たすかどうか？問題ごとに定義
        return self.t_a < self.temperatures[arg]

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stacks = []
        for i_a, t_a in enumerate(temperatures):
            for i_stack, stack in enumerate(stacks):
        """
        self.temperatures = temperatures
        ans = []
        for i_a, t_a in enumerate(temperatures):
            self.t_a = t_a
            #self.i_a = i_a
            i_b = self.meguru_bisect(i_a, len(temperatures))
            ans.append(i_b - i_a)
        return ans
        """
        """
        ans = []
        for i_a, t_a in enumerate(temperatures):
            warmer_day_exists = False
            for i_b, t_b in enumerate(temperatures[i_a+1:]):
                if t_a < t_b:
                    ans.append(1+i_b)
                    warmer_day_exists = True
                    break
            if not warmer_day_exists: 
                ans.append(0)
        return ans
        """


def q_739_top():
    if DEBUG_OUT:
        print(Solution().dailyTemperatures(
            [73,74,75,71,69,72,76,73],
        ))
        print(Solution().dailyTemperatures(
            [30,40,50,60],
        ))
        print(Solution().dailyTemperatures(
            [30,60,90]
        ))

    
if __name__ == "__main__":
    q_739_top()
