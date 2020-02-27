#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', '}':'{',']':'['}
        stack = []
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if not stack: return False
                top = stack.pop()
                if top is not dic[i]:
                    return False
        return True if not stack else False

s = Solution()
print(s.isValid("([)]"))


# @lc code=end

