#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0
        n = len(height)
        maxLeft, maxRight = [0]*n, [0]*n
        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]
        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1],height[i])
        for i in range(n-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i])
        for i in range(n):
            if min(maxLeft[i],maxRight[i]) > height[i]:
                res += min(maxLeft[i],maxRight[i]) - height[i]
        return res
        


# @lc code=end

