#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
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
            
# @lc code=end