#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        import math
        dp = [0 for _ in range(n+1)]
        dp[3] = 1
        for i in range(4,n):
            dp[i] = dp[i-1]*i
        return math.factorial(n) - dp[n]

# @lc code=end

