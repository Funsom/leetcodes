#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# 这个问题骚呀，不看答案都想不到，我说题干里给到的O(logN)是干嘛的
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
        

if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(5))

# @lc code=end

