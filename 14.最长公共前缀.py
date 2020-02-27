#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ''
        n = len(strs)
        lens = [len(i) for i in strs]
        len1 = min(lens)
        minIndex = lens.index(len1)
        p = 0
        
        while p < len1:     
            for i in range(1,n):
                    if strs[i][p] != strs[0][p]:
                        return strs[0][:p]
            p += 1
        return strs[minIndex]
# @lc code=end
'''
s = Solution()
print(s.longestCommonPrefix(["alower","flow","clight"]))
'''
