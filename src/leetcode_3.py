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
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        et = 1
        longest_sub_s = ""
        
        while True:
            sub_s = s[st:et]
            c = collections.Counter(list(sub_s))
            is_valid_sub_s = True
            for k, v in c.items():
                if v > 1:
                    st += 1
                    is_valid_sub_s = False
                    break
            
            if is_valid_sub_s:
                if len(longest_sub_s) < len(sub_s):
                    longest_sub_s = sub_s
            et += 1

            if et > len(s):
                break

        return len(longest_sub_s)


def q_3_top():
    if DEBUG_OUT:
        print(Solution().lengthOfLongestSubstring(
            "au",
        ))
        print(Solution().lengthOfLongestSubstring(
            " ",
        ))

    
if __name__ == "__main__":
    q_3_top()
