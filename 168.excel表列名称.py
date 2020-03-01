#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            n, y = divmod(n, 26) 
            res = chr(y + 65) + res
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(701))
# @lc code=end

