#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # dp[第几天][有无股票] = 最大利润
        # 以下为无限制的dp公式
        # dp[N][0] = max(dp[N-1][1] + prices[N],
        #                dp[N-1][0])
        # dp[N][1] = max(dp[N-1][0] - prices[N],
        #                dp[N-1][1])
        if not prices: return 0
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1] + prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i],dp[i-1][1])
        return dp[n-1][0]
# @lc code=end

