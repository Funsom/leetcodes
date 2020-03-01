#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        dp = [1,1]
        for i in range(2,rowIndex+1):
            next_layer = [1 for _ in range(rowIndex+1)]
            for j in range(1,i):
                next_layer[j] = dp[j] + dp[j-1]
            dp = next_layer
        return dp
# @lc code=end

