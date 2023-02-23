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
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for c in tokens:
            if len(self.stack) >= 2:
                a = self.stack[-2]
                b = self.stack[-1]

            if c=="+":
                ans = a + b
                self.stack = self.stack[:-2]
                self.stack.append(ans)
            elif c=="-":
                ans = a - b
                self.stack = self.stack[:-2]
                self.stack.append(ans)
            elif c=="*":
                ans = a * b
                self.stack = self.stack[:-2]
                self.stack.append(ans)
            elif c=="/":
                # 1 // (-10) == -1
                # int(1 / (-10)) = 0
                ans = int(a / b)
                self.stack = self.stack[:-2]
                self.stack.append(ans)
            else:  # number
                self.stack.append(int(c))

        return self.stack[0]


def q_150_top():
    if DEBUG_OUT:
        print(Solution().evalRPN(
            ["2","1","+","3","*"]
        ))
        print(Solution().evalRPN(
            ["4","13","5","/","+"]
        ))
        print(Solution().evalRPN(
            ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        ))

    
if __name__ == "__main__":
    q_150_top()
