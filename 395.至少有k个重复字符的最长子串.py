#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 找个字符串个数最少的字符
        t = min(set(s), key=s.count)
        # 最少字符的个数都大于等于k
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring(a,k) for a in s.split(t))



# @lc code=end

