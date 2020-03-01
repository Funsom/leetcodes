#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        
        import re
        # if re.search(r'^\s*$',s): return False
        return bool(re.match(r' *[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)(e[+-]?[0-9]+)? *$', s))

if __name__ == "__main__":
    s = Solution()
    print(s.isNumber('e9'))
# @lc code=end

