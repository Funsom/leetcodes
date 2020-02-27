#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP算法 dp[j][c] 代表在j状态下遇到字符c时转到的状态
        if not needle: return 0

        n = len(needle)
        X = 0

        # c有256种选择
        dp = [[ 0 for _ in range(256)] for _ in range(n)]
        # base case
        dp[0][ord(needle[0])] = 1

        for j in range(1,n):
            for c in range(256):
                dp[j][c] = dp[X][c]
            dp[j][ord(needle[j])] = j + 1
            X = dp[X][ord(needle[j])]
        j = 0
        for i in range(len(haystack)):
            j = dp[j][ord(haystack[i])]
            if j == n:
                return i - n + 1
        return -1
        



# @lc code=end

