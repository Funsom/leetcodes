#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        #牛顿迭代法
        # f(a) = a^2 - x
        a = 1.0
        while True:
            temp = 0.5*(a + x/a)
            if abs(temp - a) < 1e-2:
                return int(temp)
            a = temp
             
# @lc code=end

