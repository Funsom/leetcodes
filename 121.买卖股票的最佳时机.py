#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1] + prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i],dp[i-1][1])
        return dp[n-1][0]

# @lc code=end

