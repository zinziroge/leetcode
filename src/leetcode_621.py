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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cur_unit = 1
        last_exe_task_unit = {}
        task_done = [False] * len(tasks)

        while True:
            i_cur_task = task_done.index(False)
            cur_task = tasks[i_cur_task]
            if last_exe_task_unit.get(cur_task) is not None \
                and (cur_unit - last_exe_task_unit[cur_task]) <= n:
                # do another task 
                done_another_task = False
                for i, done in enumerate(task_done[i_cur_task+1:]):
                    another_task = tasks[i_cur_task+1+i]
                    if not done \
                        and ((another_task not in last_exe_task_unit.keys()) \
                             or (cur_unit - last_exe_task_unit[another_task]) > n):

                        last_exe_task_unit[another_task] = cur_unit
                        task_done[i_cur_task+1+i] = True
                        done_another_task = True
                        print(another_task)
                        break
                # idle
                if not done_another_task:
                    print("idle")
            else: # do cur_task
                last_exe_task_unit[cur_task] = cur_unit
                task_done[i_cur_task] = True
                print(cur_task)
            
            if i_cur_task==len(tasks) or sum(task_done[i_cur_task:])==(len(tasks) - i_cur_task): 
                break
            
            cur_unit += 1

        return cur_unit


def q_621_top():
    if DEBUG_OUT:
        print(Solution().leastInterval(
            ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2
        ))
        print()
        return

        print(Solution().leastInterval(
            tasks = ["A","A","A","B","B","B"], n = 2
        ))
        print()
        print(Solution().leastInterval(
            tasks = ["A","A","A","B","B","B"], n = 0
        ))
        print()
        print(Solution().leastInterval(
            tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
        ))
        print()

if __name__ == "__main__":
    q_621_top()
