#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            ans = max(ans,dp[i])
        return ans


# @lc code=end

