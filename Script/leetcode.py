# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:50:04 2020

@author: Illusion
"""

def reverse( x: int) -> int:
        s = list(str(x))
        n = len(s)
        L = 0 if s[0] != '-' else 1
        R = n - 1
        while L < R:
            s[L], s[R] = s[R],s[L]
            L += 1
            R -= 1
        x = int(''.join(s))
        return x if x >= -2**31 and x <= 2**31 - 1 else 0
print(reverse(-120))