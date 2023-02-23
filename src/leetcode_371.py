from itertools import product, combinations, combinations_with_replacement
import math
import random
import sys
import collections
from pathlib import Path
import bisect
import math

import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def q_371_top():
    if DEBUG_OUT:
#        q_371("""
#1 2
#"""[1:-1].split('\n'))
#
#        q_371("""
#2 3
#"""[1:-1].split('\n'))
#
#        q_371("""
#2 -3
#"""[1:-1].split('\n'))

        q_371("""
-12 -8
"""[1:-1].split('\n'))

def q_371(user_input=None):
    a, b = list(map(int, user_input.pop(0).split()))
    ans = 0
    c = 0

    for sft in range(32):  # -1024 < -1000 <= a,b <= 1000 < 1023, S12 -> bit expantion S13(ans)
        a_bit = (a & (1 << sft)) >> sft
        b_bit = (b & (1 << sft)) >> sft

        s = a_bit ^ b_bit ^ c  # sum
        c = (a_bit & b_bit) | (b_bit & c) | (c & a_bit)  # carry

        ans |= s << sft
        #print(bin(ans), sft, s, c, a_bit, b_bit)

    #print(bin(ans), ans, type(ans))
    ans = ~(ans ^ 0xffffffff)

    return ans

    
if __name__ == "__main__":
    q_371_top()
