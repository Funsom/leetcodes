#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        bins = bin(n)
        count = Counter(bins)
        return count['1']

        
# @lc code=end

