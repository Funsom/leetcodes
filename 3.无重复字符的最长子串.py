#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        res = []
        for i in range(n):
            sets = set()
            for j in range(i,n):
                if s[j] not in sets:
                    sets.add(s[j])
                else:
                    break
            res.append(len(sets))
        return max(res)
'''    
s = Solution()
print(s.lengthOfLongestSubstring('au'))
'''
# @lc code=end

