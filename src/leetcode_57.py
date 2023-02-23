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
        a = self.intervals[arg]
        if arg + 1 >= len(self.intervals):
            return False
        b = self.intervals[arg + 1]

        if a[0] < self.newInterval[0] and self.newInterval[1] < b[1]:
            return True
        else:
            return False

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if newInterval[1] < intervals[0][0]:
            intervals = [newInterval] + intervals
            return intervals
        elif intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals

        self.intervals = intervals
        self.newInterval = newInterval
        i = self.meguru_bisect(-1, len(intervals) - 2 + 1)
        if i==len(intervals) - 1:
            return intervals

        if intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i+1][0]:
            # add newInterval
            intervals.insert(i, newInterval)
        #elif intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[1]:
        else:
            # expand
            intervals[i][1] = newInterval[1]

        return intervals


def q_57_top():
    if DEBUG_OUT:
        # add
        print(Solution().insert(
            [[1,2],[3,5],[6,7],[8,10],[15,16]], [11,12]
        ))
        # merge
        print(Solution().insert(
            [[1,3],[6,9]], [2,5]
        ))
        # can not insert
        print(Solution().insert(
            [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
        ))
        # insert 1st
        print(Solution().insert(
            [[3,5],[6,7],[8,10],[12,16]], [1,2]
        ))
        # insert last
        print(Solution().insert(
            [[1,2], [3,5],[6,7],[8,10]], [12,16],
        ))

    
if __name__ == "__main__":
    q_57_top()
