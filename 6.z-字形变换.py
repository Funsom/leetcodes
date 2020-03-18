#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        for i in range(len(s)):
            n = i % 2*numRows
            if n < numRows:
                res[n].append(s[i])
            else:
                res[2*numRows - n - 1].append(s[i])
        print(res)
        return ''.join([j for i in res for j in i])

if __name__ == "__main__":
    s = Solution()
    strs = "PAYPALISHIRING"
    res = s.convert(strs,3)
    print(res)

# @lc code=end

