#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        from collections import Counter
        from functools import reduce
        from math import gcd
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2

if __name__ == "__main__":
    s = Solution()
    res = s.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2])
    print(res)
# @lc code=end

