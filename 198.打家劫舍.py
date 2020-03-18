#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        # dp[i] = x 从第i家开始抢，可以抢到的最多的钱
        dp = [0 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i+1],nums[i]+dp[i+2])
        return dp[0]

# @lc code=end

