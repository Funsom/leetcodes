#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        L, R = 0, n-1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
# @lc code=end

