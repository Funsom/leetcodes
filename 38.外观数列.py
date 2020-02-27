#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        dp = ["" for _ in range(n)]
        dp[0] = '1'
        for i in range(1,n):
            j = 0
            count = 1
            while j < len(dp[i-1])-1:
                if dp[i-1][j] == dp[i-1][j+1]:
                    count += 1
                    j += 1
                else:
                    dp[i] += (str(count) + dp[i-1][j])
                    count = 1
                    j += 1
            dp[i] += (str(count) + dp[i-1][j])
        return dp[n-1]

# @lc code=end

