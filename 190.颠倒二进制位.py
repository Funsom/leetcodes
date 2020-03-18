#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        lens = len(bin(n)[2:])
        ans = '0'*(32-lens) + bin(n)[2:]
        ans = ans[::-1]
        return int(ans,2)

        
# @lc code=end

